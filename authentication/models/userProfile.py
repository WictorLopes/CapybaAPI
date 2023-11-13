from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmation_token = models.CharField(max_length=100, null=True, blank=True)


