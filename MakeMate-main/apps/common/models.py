from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username