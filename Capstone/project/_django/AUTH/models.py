from django.db.models import *
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Account(AbstractUser):
    avatar = ImageField(default='')
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=16)
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    email = EmailField(max_length=40, unique=True)
    display_name = CharField(max_length=20)
    regcode = CharField(max_length=4, unique=True)
    phone = CharField(max_length=13)
    donation = IntegerField(default=0)
    wallet = IntegerField(default=0)
    # open_requests = ForeignKey(to, on_delete)

    def __str__(self):
        legal_name = f'{self.first_name.title()} {self.last_name.title()}'
        return legal_name


class Patron(Model):
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    regcode = CharField(max_length=4, unique=True)
    donation = IntegerField(default=0)
    registered = BooleanField(default=False)

    def __str__(self):
        legal_name = f'{self.first_name.title()} {self.last_name.title()}'
        return legal_name
