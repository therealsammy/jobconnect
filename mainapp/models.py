from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add any additional fields you need for user profiles
    pass


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
