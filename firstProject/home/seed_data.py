from home.models import *
import time
from faker import Faker
faker = Faker()
import random
# record start time
start = time.time()

department1 = Department.objects.create(department_name="Computer Science")
department2 = Department.objects.create(department_name="Electrical Engineering")
# Create colleges
college1 = College.objects.create(college_name="MIT")
college2 = College.objects.create(college_name="CMU")
college3 = College.objects.create(college_name="Stanford")
# create skills
coding = Skills.objects.create(skill_name="coding")
design = Skills.objects.create(skill_name="design")

def seed_db_bulk_create(num_records):
    students = []
    for _ in range(num_records):
        # Generate random student data
            name = faker.name()
            gender = random.choice([Student.MALE, Student.FEMALE])
            email = faker.email()
            date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=25)
            phone_number = faker.phone_number()[:10]

            # Randomly assign college and department
            college = random.choice([college1, college2, college3])
            department = random.choice([department1, department2])
    
            # Create and save the student record
            student = Student(
                name=name,
                gender=gender,
                email=email,
                date_of_birth=date_of_birth,
                phone_number=phone_number,
                college=college,
                department=department,
            )
            students.append(student)
            # Add skills to the student
    created_students = Student.objects.bulk_create(students)
    for student in created_students:
        student.skill.add(coding, design)

seed_db_bulk_create(1000)
# record end time
end = time.time()
# Print the difference between start and end time in milliseconds
execution_time = (end - start) * 10**3
print("The time of execution of the above program is:", execution_time, "ms")



# def seed_db(num_records):
#     for _ in range(num_records):
#         # Generate random student data
#             name = faker.name()
#             gender = random.choice([Student.MALE, Student.FEMALE])
#             email = faker.email()
#             date_of_birth = faker.date_of_birth(minimum_age=18, maximum_age=25)
#             phone_number = faker.phone_number()[:10]

#             # Randomly assign college and department
#             college = random.choice([college1, college2, college3])
#             department = random.choice([department1, department2])
    
#             # Create and save the student record
#             student = Student(
#                 name=name,
#                 gender=gender,
#                 email=email,
#                 date_of_birth=date_of_birth,
#                 phone_number=phone_number,
#                 college=college,
#                 department=department,
#             )
#             student.save()
#             # Add skills to the student
#             student.skill.add(coding, design)


# # record end time
# end = time.time()
# # Print the difference between start and end time in milliseconds
# execution_time = (end - start) * 10**3
# print("The time of execution of the above program is:", execution_time, "ms")
