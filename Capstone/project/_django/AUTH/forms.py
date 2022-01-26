from django.forms import ModelForm
from .models import *


class Register(ModelForm):
    # form to enter registration code
    class Meta:
        model = Account
        fields = ['regcode']


class Verified(ModelForm):
    # form to create user if regcode is valid
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'regcode', 'username',
                  'password', 'display_name', 'phone', 'email']


class Login(ModelForm):
    # login form
    class Meta:
        model = Account
        fields = ['username', 'password']
