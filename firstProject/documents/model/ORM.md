## Object relational mapping(ORM):

we use databases to store our data and SQL queries to update or add data to the database, as our app grows, so does the SQL queries gets more complex.

Object-Relational Mapping (ORM) is a programming technique that allows us to interact with a relational database using an object-oriented paradigm. In the context of Django, the ORM abstracts the database interactions, allowing us to work with Python objects instead of SQL queries. This makes it easier to write and maintain database code, as it allows developers to use Python syntax and concepts.

django provides an ORM, where it automatically creates required SQL queries.
ORM facilitates interaction between the programming language and database.

It allows us to use `SQL` queries without writing sql queries.
A structured map is created internally by ORM that generated SQL queries.

### Features

`Model Definition`: we define our database schema using Python classes (models), which represent tables in the database.

`Querying`: we can perform complex queries using Python syntax. The ORM translates these queries into SQL for us.

`Data Manipulation`: we can create, read, update, and delete records using methods provided by the ORM.

`Database Abstraction`: The ORM supports multiple database backends (e.g., PostgreSQL, MySQL, SQLite), allowing us to switch databases with minimal code changes.

#### Query set

- adding each row entry for a given model creates an object.
- query set is a collection of objects for a given model.
- django uses query set to retrieve and manipulate the objects.

In Django models, the `id` field is automatically created by default as the primary key for each model unless specified otherwise

```py
from django.db import models
class Courses(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length =100)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.duration
```

Creating a custom id.

```py
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  # Custom primary key
```

```py
python manage.py shell
from home.models import Courses
Courses.objects.all() ## It returns a query set object.
```

- for every sql query to be constructed, there is a corresponding command and these commands are part of `QuerySet API`

`SQL QUERY`

```sh
SELECT * FROM COURSES WHERE name="ai"
```

`QuerySet API`

```py
Courses.objects.filter(name="ai")
```

## How to add an entry using django shell

```py
python manage.py shell
from home.models import Courses  # Adjust the import according to your app name
new_course = Courses(
    name="Introduction to Django",
    duration="3 months",
    price=300
)
new_course.save()  # This saves the new entry to the database
Courses.objects.all()
```

To see the latest change on `pgadmin` interface, go to your database, right click and then click on `refresh`.

`exit()` or `CTR+D` on MACOS to exit the shell.

```sql
-- Create the User table with first_name and last_name fields
CREATE TABLE User (
id SERIAL PRIMARY KEY, -- Auto-incrementing ID for each user
first_name VARCHAR(90) NOT NULL,
last_name VARCHAR(90) NOT NULL
);

-- Create the Product table with name, price, and availability status
CREATE TABLE Product (
id SERIAL PRIMARY KEY, -- Auto-incrementing ID for each product
name VARCHAR(200) NOT NULL,
price DECIMAL(10, 2) NOT NULL, -- Decimal field with a max of 10 digits, 2 of which are after the decimal point
available BOOLEAN DEFAULT TRUE -- Boolean field, default is 'true'
);

-- CRUD operations:

-- Create a new user (John Doe)
INSERT INTO User (first_name, last_name)
VALUES ('John', 'Doe');

-- Read a user by id
SELECT \* FROM User WHERE id = 1;

-- Read all users
SELECT \* FROM User;

-- Update a user's first name
UPDATE User
SET first_name = 'Jane'
WHERE id = 1;

-- Delete a user by id
DELETE FROM User WHERE id = 1;

-- Create a new product
INSERT INTO Product (name, price, available)
VALUES ('Laptop', 1200.00, TRUE);

-- Read a product by id
SELECT \* FROM Product WHERE id = 1;

-- Read all products
SELECT \* FROM Product;

-- Update a product's price
UPDATE Product
SET price = 999.99
WHERE id = 1;

-- Delete a product by id
DELETE FROM Product WHERE id = 1;


```
