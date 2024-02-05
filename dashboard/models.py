from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Order(models.Model):
#     product_category = models.CharField(max_length=20)
#     payment_method = models.CharField(max_length=50)
#     shipping_cost = models.CharField(max_length=50)
#     unit_price = models.DecimalField(max_digits=5, decimal_places=2)


class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    #members = models.ManyToManyField(Member, related_name='clubs')


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()


