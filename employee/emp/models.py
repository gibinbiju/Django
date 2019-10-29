from django.db import models
class Desig(models.Model):
    designation=models.CharField(max_length=120)
    def __str__(self):
        return self.designation
class Company(models.Model):
    companyname=models.CharField(max_length=120)#
    def __str__(self):
        return self.companyname
class Employee(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    desig=models.ForeignKey(Desig,on_delete=models.CASCADE)
    ename=models.CharField(max_length=20)#
    esal=models.IntegerField()

# Create your models here.
