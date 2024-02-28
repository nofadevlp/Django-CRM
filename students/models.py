from django.db import models

# Create your models here.
class Student(models.Model):
    std_no= models.PositiveIntegerField()
    first_name= models.CharField(max_length=38)
    last_name= models.CharField(max_length=38)
    email = models.EmailField(max_length=150)
    field_of_study= models.CharField(max_length=50)
    gpa=models.FloatField()
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'