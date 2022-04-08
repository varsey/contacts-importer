from django.db import models
from django.contrib.auth.models import User

class ContactsDB(models.Model):
    Name = models.CharField(max_length=200, blank=True)
    DOB = models.DateField(blank=True)
    Phone = models.CharField(max_length=200, blank=True)
    Address = models.TextField(blank=True)
    CreditCard = models.IntegerField(blank=True)
    Franchise = models.CharField(max_length=200, blank=True)
    Email = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Name

