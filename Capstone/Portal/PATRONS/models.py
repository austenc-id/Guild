from django.db.models import *
from django.contrib.auth.models import AbstractUser


class Patron(Model):
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    email = EmailField()
    regcode = CharField(max_length=4, unique=True)
    donation = DecimalField(default=0, max_digits=8, decimal_places=2)
    unlimited = BooleanField(default=False)
    registered = BooleanField(default=False)

    def full_name(self):
        """Returns the user's full name"""
        full_name = f'{self.first_name.title()} {self.last_name.title()}'
        return full_name

    def __str__(self):
        return self.full_name()


class User(AbstractUser):
    from colorful.fields import RGBColorField as ColorField
    user_id = CharField(max_length=6)
    username = CharField(max_length=12, unique=True)
    password = CharField(max_length=88)
    favorite_color = ColorField(default='#000000')
    use_favorite_color = BooleanField(default=False, help_text='would you like to set your favorite color as the default link color?')
    regcode = CharField(max_length=4, unique=True)
    donation = DecimalField(default=0, max_digits=8, decimal_places=2)
    tokens = IntegerField(default=0)
    login_count = IntegerField(default=0)
    confirm_profile = BooleanField(default=True)

    def __str__(self):
        return f'{self.username}'