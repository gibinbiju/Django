from django.db import models

# Create your models here.
from django import forms
from datetime import datetime

class users(models.Model):
    username=models.CharField(max_length=120)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=12)
    pwd=models.CharField(max_length=150)

    def __str__(self):
        return self.username
class category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class expense(models.Model):
    name=models.ForeignKey(users,on_delete=models.CASCADE)
    category_name=models.ForeignKey(category,on_delete=models.CASCADE)
    amount=models.FloatField()
    dates=models.DateField(default=datetime.now)
    def __str__(self):
        template = '{0.name} {0.category_name} {0.dates} {0.amount}'
        return template.format(self)

