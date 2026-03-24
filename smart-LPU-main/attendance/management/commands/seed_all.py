import random
from datetime import date, time as dt_time
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from attendance.models import (
    Student, Course, Enrollment, Section, Block, Classroom, 
    FacultyProfile, SectionCourseFaculty, StudentSection, AttendanceSession
)
from food.models import Stall, FoodItem, BreakSlot, StallOwner

User = get_user_model()

class Command(BaseCommand):
    help = "Seed the database with comprehensive sample data for Shannu Management"

    def handle(self, *args, **options):
        self.stdout.write("Starting comprehensive seed process...")

        # 1. Sections
        self.stdout.write("Seeding Sections...")
        sections = []
        for name in ["Section A", "Section B", "Section C"]:
            section, _ = Section.objects.get_or_create(name=name, defaults={"year": 2, "semester": 4})
            sections.append(section)

        # 2. Courses
        self.stdout.write("Seeding Courses...")
        courses = [
            {"code": "CSE101", "name": "Data Structures", "sem": 3, "year": 2},
            {"code": "CSE202", "name": "Operating Systems", "sem": 4, "year": 2},
            {"code": "AIML301", "name": "Machine Learning", "sem": 5, "year": 3},
            {"code": "MBA101", "name": "Principles of Management", "sem": 1, "year": 1},
        ]
        db_courses = []
        for c in courses:
            course, _ = Course.objects.get_or_create(
                code=c["code"], 
                defaults={"name": c["name"], "semester": c["sem"], "year": c["year"]}
            )
            db_courses.append(course)

        # 3. Blocks & Classrooms
        self.stdout.write("Seeding Blocks & Classrooms...")
        blocks_data = [
            ("CSE-027", "CSE Block 27"),
            ("MBB-001", "Business Block 1"),
        ]
        for code, name in blocks_data:
            block, _ = Block.objects.get_or_create(code=code, defaults={"name": name})
            for i in range(1, 4):
                Classroom.objects.get_or_create(
                    block=block, 
                    room_number=f"{code}-{i}01", 
                    defaults={"capacity": 60, "room_type": "classroom"}
                )

        # 4. Faculty Users & Profiles
        self.stdout.write("Seeding Faculty...")
        faculty_data = [
            {"username": "prof.sharma", "email": "sharma@csr.local", "name": "Dr. Sharma", "dept": "CSE"},
            {"username": "prof.reddy", "email": "reddy@csr.local", "name": "Dr. Reddy", "dept": "MBA"},
        ]
        for f in faculty_data:
            u, created = User.objects.get_or_create(
                username=f["username"],
                defaults={
                    "email": f["email"],
                    "password": make_password("Prof@123"),
                    "is_staff": True,
                    "first_name": f["name"]
                }
            )
            FacultyProfile.objects.get_or_create(
                user=u,
                defaults={
                    "department": f["dept"], 
                    "designation": "Associate Professor",
                    "employee_id": f"EMP-{u.id}-{random.randint(1000, 9999)}"
                }
            )

        # 5. Students
        self.stdout.write("Seeding Students...")
        students_data = [
            {"reg": "123001", "name": "Aman Kumar", "email": "aman@student.local"},
            {"reg": "123002", "name": "Priya Singh", "email": "priya@student.local"},
            {"reg": "123003", "name": "Rahul Verma", "email": "rahul@student.local"},
            {"reg": "123004", "name": "Sneha Rao", "email": "sneha@student.local"},
            {"reg": "123005", "name": "Vikram Das", "email": "vikram@student.local"},
        ]
        db_students = []
        for s in students_data:
            student, _ = Student.objects.get_or_create(
                registration_number=s["reg"],
                defaults={
                    "full_name": s["name"],
                    "email": s["email"],
                    "year": 2,
                    "semester": 4,
                    "department": "CSE" if int(s["reg"]) % 2 == 0 else "MBA"
                }
            )
            db_students.append(student)
            # Assign to Section A for now
            StudentSection.objects.get_or_create(student=student, section=sections[0])

        # 6. Enrollments
        self.stdout.write("Seeding Enrollments...")
        for student in db_students:
            # Everyone enrolled in Data Structures and OS
            Enrollment.objects.get_or_create(student=student, course=db_courses[0])
            Enrollment.objects.get_or_create(student=student, course=db_courses[1])

        # 7. Food App: Break Slots
        self.stdout.write("Seeding Food App Slots...")
        slots_data = [
            ("Morning Break", dt_time(10, 30), dt_time(11, 0)),
            ("Lunch Break", dt_time(13, 0), dt_time(14, 0)),
            ("Evening Break", dt_time(16, 0), dt_time(16, 30)),
        ]
        for name, start, end in slots_data:
            BreakSlot.objects.get_or_create(name=name, defaults={"start_time": start, "end_time": end})

        # 8. Food App: Stalls & Items
        self.stdout.write("Seeding Food App Stalls & Items...")
        stalls_data = [
            {"name": "Main Canteen", "location": "Block 27 Ground Floor"},
            {"name": "Juice Bar", "location": "Student Plaza"},
        ]
        for s in stalls_data:
            stall, _ = Stall.objects.get_or_create(name=s["name"], defaults={"location": s["location"]})
            # Create a vendor user if not exists
            vendor_user, _ = User.objects.get_or_create(
                username=f"vendor_{stall.id}",
                defaults={"password": make_password("Vendor@123"), "is_staff": True}
            )
            StallOwner.objects.get_or_create(user=vendor_user, stall=stall)
            
            # Items
            if "Canteen" in stall.name:
                items = [
                    ("Masala Dosa", 50.00, "Breakfast"),
                    ("Veg Thali", 80.00, "Lunch"),
                    ("Paneer Puff", 25.00, "Snacks"),
                ]
            else:
                items = [
                    ("Orange Juice", 40.00, "Beverages"),
                    ("Mixed Fruit Bowl", 60.00, "Healthy"),
                ]
            
            for i_name, i_price, i_cat in items:
                FoodItem.objects.get_or_create(
                    name=i_name, 
                    stall=stall,
                    defaults={
                        "price": i_price, 
                        "category": i_cat, 
                        "stall_name": stall.name,
                        "location": stall.location
                    }
                )

        self.stdout.write(self.style.SUCCESS("Comprehensive seeding completed successfully!"))
