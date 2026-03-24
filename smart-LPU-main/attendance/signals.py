from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Student, Section, Course, Enrollment, StudentSection, CourseOffering

@receiver(post_save, sender=StudentSection)
def sync_student_enrollments_on_section_change(sender, instance, created, **kwargs):
    """
    When a student is added to or moved to a section, 
    automatically enroll them in all courses assigned to that section.
    """
    student = instance.student
    section = instance.section
    
    # Get all courses assigned to this section
    section_courses = section.courses.all()
    
    for course in section_courses:
        Enrollment.objects.get_or_create(student=student, course=course)

@receiver(m2m_changed, sender=Section.courses.through)
def sync_section_courses_to_students(sender, instance, action, pk_set, **kwargs):
    """
    When courses are added to a section, automatically enroll all 
    students in that section into the new courses.
    """
    if action == "post_add":
        section = instance
        courses = Course.objects.filter(pk__in=pk_set)
        students = Student.objects.filter(section_mapping__section=section)
        
        for course in courses:
            for student in students:
                Enrollment.objects.get_or_create(student=student, course=course)

@receiver(post_save, sender=CourseOffering)
def ensure_enrollment_on_offering_creation(sender, instance, created, **kwargs):
    """
    If a CourseOffering is created for a section, ensure all students 
    in that section are enrolled in that course.
    """
    if created and instance.section:
        course = instance.course
        section = instance.section
        students = Student.objects.filter(section_mapping__section=section)
        
        for student in students:
            Enrollment.objects.get_or_create(student=student, course=course)
