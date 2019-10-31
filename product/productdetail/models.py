from django.db import models
class product(models.Model):
    pname=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    price=models.IntegerField()
    spec=models.CharField(max_length=50)
# Create your models here.
