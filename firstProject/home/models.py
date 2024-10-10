from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class BaseModel(models.Model):
    field_from_base_model = models.CharField(max_length=102, default="BASE FIELD")
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.field_from_base_model


class Product(BaseModel):
    product_name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.product_name}")
        super(Product, self).save(*args, **kwargs)
 

class College(BaseModel):
    college_name = models.CharField(max_length=100)
    def __str__(self):
        return self.college_name
    
class Department(BaseModel):
    department_name = models.CharField(max_length=100)
    def __str__(self):
        return self.department_name
    
    
class Skills(BaseModel):
    skill_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.skill_name
    
class Student(BaseModel):
    student_id = models.CharField(max_length=100, blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)
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
    is_deleted = models.BooleanField(default=False)

    class Meta:
        # it will overwrite the home_student name
        db_table= "student_table"
        # order them by name when querying.
        ordering = ["name"]

    def __str__(self):
        return self.name



class ContactModel(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    comment = models.CharField(max_length=10000)

    class Meta:
        db_table="home_contact_form"