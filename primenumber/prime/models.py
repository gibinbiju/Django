from django.db import models

class primesum(models.Model):
    lower=models.IntegerField()
    upper=models.IntegerField()
    def __str__(self):
        return self.lower
