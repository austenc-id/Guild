from django.forms import ModelForm
from .models import *


class Register(ModelForm):
    class Meta:
        model = Account
        fields = ['regcode']


class Verified(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'regcode', 'username',
                  'password', 'display_name', 'phone', 'email']


class Login(ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
