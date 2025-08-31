from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank= True)
    file = models.FileField()

class Product(models.Model):
    pass