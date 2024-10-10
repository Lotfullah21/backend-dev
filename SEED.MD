```sh
pip install Faker
```

```py
import faker
from faker import Faker
fake = Faker()
fake.name()
```

[faker-docs](https://pypi.org/project/Faker/)

```py
from faker import Faker
from home.models import College, Student
faker = Faker()

for _ in range(20):
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
    student.save()
    # Add skills to the student
    student.skill.add(coding, design)
```
