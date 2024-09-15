from django.db import models

# Create your models here.

# wongalethu/models.py
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

