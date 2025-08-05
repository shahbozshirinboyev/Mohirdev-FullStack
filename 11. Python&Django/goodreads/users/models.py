from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
  avatar = models.ImageField(default='default_avatar.jpg')
