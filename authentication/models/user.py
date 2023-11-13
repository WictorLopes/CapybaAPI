from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from rest_framework.authtoken.models import Token

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)  
    email = models.EmailField(unique=True) 
    token = models.OneToOneField(Token, on_delete=models.CASCADE,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
