from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=128)
    address=models.CharField(max_length=128)
    course=models.CharField(max_length=20)


    def __str__(self):
        return self.name