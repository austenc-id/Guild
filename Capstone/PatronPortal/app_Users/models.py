from django.db.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=88)
    regcode = CharField(max_length=4, unique=True)

    def __str__(self):
        return f'{self.username}'
