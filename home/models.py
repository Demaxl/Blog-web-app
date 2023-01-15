from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    profile_photo = models.ImageField(upload_to="home/profile_pic/", blank=True, default="static/default.jpg")
    joined_date = models.DateField(auto_now_add=True)
    about = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET("Deleted"), related_name="articles")
    publish_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=128)        
    body = models.TextField()                                                              
    cover_image = models.ImageField(upload_to="home/cover_image/", blank=True)

    def __str__(self):
        return f"{self.subject} by {self.author}"
    