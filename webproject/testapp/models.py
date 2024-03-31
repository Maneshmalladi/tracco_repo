# Create your models here.
from django.db import models
class RegModel(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    gender=models.CharField(max_length=15)
    password=models.CharField(max_length=30)
    rpassword=models.CharField(max_length=30)
