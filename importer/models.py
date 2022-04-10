from django.db import models
from django.contrib.auth.models import User


class Contacts(models.Model):
    Name = models.CharField(max_length=200)
    DOB = models.DateField()
    Phone = models.CharField(max_length=200)
    Address = models.TextField()
    CreditCard = models.IntegerField()
    Franchise = models.CharField(max_length=40)
    Email = models.CharField(max_length=100)


class CsvJobs(models.Model):
    job_id = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True)
