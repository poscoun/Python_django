from django.db import models

# main models.py

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True) # 제약조건
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)

