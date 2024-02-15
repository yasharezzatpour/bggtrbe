from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255 , null=True)
    email = models.EmailField(max_length=255 , unique= True , null=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(unique=True , max_length=255)
    info = models.TextField(null= True)
    signInDate = models.DateField( default='2023-10-10')
    urlToProfileImage = models.CharField(max_length=255 , null=True)
    rating = models.IntegerField(null=True)
    jobTitle = models.CharField(max_length=255 , null= True)
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

