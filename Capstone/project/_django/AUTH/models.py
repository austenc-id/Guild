from django.db.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Account(AbstractUser):
    display_name = CharField(max_length=20)
    regcode = CharField(max_length=4)
    phone = CharField(max_length=13)
    wallet = IntegerField(default=0)
