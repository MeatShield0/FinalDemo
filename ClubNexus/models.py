from django.db import models
# Create your models here.
from django.db import models
from datetime import date
import uuid
# models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here


class ClubMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_status = models.BooleanField(default=True)
    # Add more fields as needed


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



