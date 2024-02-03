from django.db import models

# Create your models here.

from django.db import models
from datetime import date
import uuid

# Create your models here


# models.py
from django.db import models

class ClubMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_status = models.BooleanField(default=True)
    # Add more fields as needed


