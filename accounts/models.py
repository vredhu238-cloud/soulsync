from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
        blank=True,
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Yahan change kiya hai: JSONField ki jagah TextField
    interests = models.TextField(blank=True, default="") 

    def __str__(self):
        return self.username