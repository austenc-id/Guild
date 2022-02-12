from django.db.models import *
from django.contrib.auth.models import AbstractUser
from .utils import generators as gen

# Create your models here.


class User(AbstractUser):
    user_id = CharField(max_length=6)
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=88)
    regcode = CharField(max_length=4, unique=True)

    def __str__(self):
        return f'{self.username}'

    def set_user_id(self):
        self.user_id = gen.digit_code(6)
