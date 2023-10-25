from django.db import models
from django.contrib.auth.models import User


class PalindromeGame(models.Model):
    word = models.CharField(max_length=255)
    attempts = models.PositiveIntegerField(default=0)
    is_palindrome = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)

