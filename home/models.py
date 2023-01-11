from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)
    joined_date = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=1000)

class Blog(models.Model):
    pass
