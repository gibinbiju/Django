from django.db import models
from django.shortcuts import render
class detail(models.Model):
    name=models.CharField(max_length=25)
    addr=models.CharField(max_length=120)
    mob=models.IntegerField(max_length=10)
    course=models.CharField(max_length=20)
