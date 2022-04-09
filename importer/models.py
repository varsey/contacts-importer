from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.DateField()
    Phone = models.CharField(max_length=200)
    Address = models.TextField()
    CreditCard = models.IntegerField(max_length=19)
    Franchise = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)
