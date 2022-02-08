from django.forms import ModelForm, TextInput
from .models import *


class Login(ModelForm):
    # input patron data
    class Meta:
        model = User
        fields = ['username', 'password']
