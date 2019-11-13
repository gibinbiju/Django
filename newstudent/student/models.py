from django.db import models
from django.contrib.auth.models import User




class Course(models.Model):
    coursename=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.coursename

class Batch(models.Model):
    batchname=models.CharField(max_length=100,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.batchname
# class student(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user
class User(models.Model):
    username=models.CharField(max_length=20,blank=False)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=30,blank=False,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,blank=False)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE,blank=False)
    def __str__(self):
        return self.username

class Feedback(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE,blank=False)
    cname=models.ForeignKey(Course,on_delete=models.CASCADE,blank=False)
    bname=models.ForeignKey(Batch,on_delete=models.CASCADE,blank=False)
    feed=models.CharField(max_length=500,blank=False)
    def __str__(self):
        return self.feed
