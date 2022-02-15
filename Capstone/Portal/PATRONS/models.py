from django.db.models import *
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from colorful.fields import RGBColorField as ColorField

from utils import generators as gen


class Patron(Model):
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    email = EmailField()
    regcode = CharField(max_length=4, unique=True)
    donation = DecimalField(default=0, max_digits=8, decimal_places=2)
    unlimited = BooleanField(default=False)
    registered = BooleanField(default=False)

    def legal_name(self):
        legal_name = f'{self.first_name.title()} {self.last_name.title()}'
        return legal_name

    def __str__(self):
        return self.legal_name()


class User(AbstractUser):
    user_id = CharField(max_length=6)
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=88)
    favorite_color = ColorField(default='#000000')
    use_favorite_color = BooleanField(
        default=False, help_text='would you like to set your favorite color as the default link color?')
    regcode = CharField(max_length=4, unique=True)
    donation = DecimalField(default=0, max_digits=8, decimal_places=2)
    tokens = IntegerField(default=0)
    login_count = IntegerField(default=0)
    confirm_profile = BooleanField(default=True)

    def __str__(self):
        return f'{self.username}'


# class Profile(Model):
#     user = OneToOneField(get_user_model(), on_delete=CASCADE)
#     favorite_color = CharField(max_length=6, default='000000')

#     def __str__(self):
#         return self.user.username
