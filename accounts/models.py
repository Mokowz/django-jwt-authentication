from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=255, blank=True, null=True)
  last_name = models.CharField(max_length=255, blank=True, null=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []