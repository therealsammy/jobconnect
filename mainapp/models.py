from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SplitCharField(models.CharField):
    def split(self, separator=','):
        return [item.strip() for item in self.split(separator) if item.strip()]


class User(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField()
    skills = SplitCharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='mainapp_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='mainapp_users', blank=True)


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experiences')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # ... other fields specific to the experience


class Meta:
    ordering = ['-start_date']  # Optional: ordering experiences by start date


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
