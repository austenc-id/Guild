from django.forms import *
from .models import *


class Login(ModelForm):
    # input patron data
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': PasswordInput()}


class Update(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'New Username',
            'password': 'New Password'
        }


class Register(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'regcode']
