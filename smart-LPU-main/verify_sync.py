import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartlpu.settings')
django.setup()

from attendance.models import Student, Section, Course, Enrollment, StudentSection

def test_sync():
    print("Starting verification...")
    
    # 1. Setup - Get or create a section and course
    section, _ = Section.objects.get_or_create(name="Sync Test Section")
    course, _ = Course.objects.get_or_create(code="SYNC101", defaults={"name": "Sync Test Course"})
    
    # Associate course with section
    section.courses.add(course)
    
    # 2. Test - Create a student and assign to section
    student, _ = Student.objects.get_or_create(
        registration_number="999999", 
        defaults={"full_name": "Sync Tester"}
    )
    
    print(f"Assigning student {student.registration_number} to section {section.name}...")
    StudentSection.objects.update_or_create(student=student, defaults={"section": section})
    
    # 3. Verify - Check if enrollment was created automatically
    enrolled = Enrollment.objects.filter(student=student, course=course).exists()
    
    if enrolled:
        print("SUCCESS: Student was automatically enrolled in the section course!")
    else:
        print("FAILURE: Student was NOT enrolled automatically.")

    # 4. Clean up (optional)
    # student.delete()
    # section.delete()
    # course.delete()

if __name__ == "__main__":
    test_sync()
