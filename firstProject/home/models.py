from django.db import models
# Create your models here.
import uuid

class College(models.Model):
    college_name = models.CharField(max_length=100)
    
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    
class Student(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True,blank=True)
    skill = models.ManyToManyField(Skills)
    MALE = 'Male'
    FEMALE = 'Female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField()
    date_of_birth = models.DateField()
    student_registration = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=123)
    password = models.CharField(max_length=120)
    def __str__(self):
        return self.name
    
    
