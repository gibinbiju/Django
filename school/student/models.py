from django.db import models
#from django.contrib.auth.models import User




class Course(models.Model):
    coursename=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.coursename

class Batch(models.Model):
    batchname=models.CharField(max_length=100,unique=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.batchname
class User(models.Model):
    username=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    def __str__(self):
        return self.username

class Feedback(models.Model):
    cname=models.ForeignKey(Course,on_delete=models.CASCADE)
    bname=models.ForeignKey(Batch,on_delete=models.CASCADE)
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    feed=models.TextField(max_length=500)
    def __str__(self):
        return self.feed
