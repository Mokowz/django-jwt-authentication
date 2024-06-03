from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=20, blank=True, null=True)
  author = models.CharField(max_length=20, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
