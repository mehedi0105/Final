from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

user_type = (
    ('seller','seller'),
    ('buyer','buyer'),
    ('admin','admin'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=50,choices=user_type)
