from django.db import models

# Create your models here.
class ToDo(models.Model):
    contents = models.CharField(max_length=255)