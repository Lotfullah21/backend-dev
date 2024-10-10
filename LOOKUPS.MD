## Lookups

```py
students = Student.objects.all()
students.count()
# By default ordering is done in ascending order
students =  Student.objects.all().order_by("date_of_birth")
# adding - fetches all data in descending order
students =  Student.objects.all().order_by("-date_of_birth")
```

```py
for student in students:
    print(f"name: {student.name} dob: {student.date_of_birth}")
```

fetch all the name starting with `Joshua`

# Filter

### Single filter

```py
# get the name that is exactly joseph
student = Student.objects.filter(name="Joseph")
# get the name that includes joseph
student = Student.objects.filter(name__icontains="Joseph")
student = Student.objects.filter(email__icontains="ali")
for s in student:
    print(f"{s.name} {s.email}")
```

### Multiple filter

```py
students = Student.objects.filter(email__icontains="ali", gender__icontains="Male")
 for s in students:
    print(f"{s.name} {s.gender}")
```

`exclude`: give me the following that does not include the property added to `exclude` function.

```py
students = Student.objects.filter(email__icontains="ali").exclude(gender="Male")
students = Student.objects.filter(gender="Female", name__icontains="Joseph").order_by("name")
```

If we are having a field like age and we want to get age > or < a certain number, we can use

```py
students = Student.objects.filter(age__gte=34) # age>=34
students = Student.objects.filter(age__lte=34) # age<=34
students = Student.objects.filter(age__gte=28,age__lte=34) # 28=<age<=34
```

#### Starts with and ends with

```py
students = Student.objects.filter(email__icontains="ali").exclude(gender="Male")
students = Student.objects.filter(gender="Female",name__startswith="Ali")
students = Student.objects.filter(gender=Student.FEMALE).exclude(name__startswith="A").exclude(name__startswith="B")

from django.db.models import Q

# List of starting letters
starting_letters = ['A', 'B', 'C']  # Add more letters as needed

# Create Q objects for each letter
queries = Q()
for letter in starting_letters:
    queries |= Q(name__startswith=letter)

# Now filter students based on the constructed queries
students = Student.objects.filter(gender=Student.FEMALE).exclude(queries)

```

### gte on date

```py
student = Student.objects.filter(date_of_birth="2003-01-20")
student = Student.objects.filter(date_of_birth__gte="2003-01-20") # younger folks

```

### filtering foreign key.

```py
student = Student.objects.filter(department__department_name="Computer Science")
student.count()
department = Department.objects.all()
for d in department:
    s = Student.objects.filter(department=d)
    print(f"Student count: {s.count()} Deprtment: {d.department_name}")
```

```py
s = Student.objects.filter(college__college_name__icontains="CMU")
s.count()
```

```py
student = Student.objects.filter(email__endswith="gmail.com")
student.count()
```

## And Logical operation

By adding `,` between our lookup fields, we can filter the data based on the given conditions and only if all the lookup fields evaluate to True, then return the data.

```py

student = Student.objects.filter(email__endswith="example.org", date_of_birth__gte="1998-02-03")
student.count() # 1221
```

## Or logical operation

If either of the lookup field matches, return the record.
Q is a class used to construct complex queries by combining query conditions using logical operators like AND, OR, and NOT
we are using implicit AND logic between multiple conditions. However, Q allows us to explicitly perform more advanced queries, like OR conditions, which aren't directly possible with simple filtering methods.

```py
from django.db.models import Q
student = Student.objects.filter(Q(date_of_birth__gte="2008-01-03")|Q(name__startswith="Joseph"))
```

```py
# get the distinct names
Student.objects.all().distinct("name")
```
