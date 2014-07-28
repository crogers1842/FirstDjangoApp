from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    date_of_birth = models.DateField()
    REQUIRED_FIELDS = ['date_of_birth']
