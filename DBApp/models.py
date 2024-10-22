from django.db import models

# Create your models here.

class Teacher (models.Model):
    T_id = models.IntegerField(null=True)
    full_name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    qualification= models.CharField(max_length=20)
    address = models.TextField()
    mobile_no = models.CharField(max_length=15)

class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()    

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE,related_name='courses')
    teacher = models.ForeignKey(CourseCategory, on_delete=models.CASCADE,related_name='taught_courses')
    title = models.CharField(max_length=100)
    description = models.TextField()  

class Student(models.Model):
    S_id = models.IntegerField()
    full_name = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    qualification= models.CharField(max_length=20)
    address = models.TextField()
    mobile_no = models.IntegerField()
    interested_categories = models.TextField()




