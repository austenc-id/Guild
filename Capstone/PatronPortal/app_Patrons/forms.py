from django.forms import ModelForm, TextInput
from .models import *


class NewPatron(ModelForm):
    # * input patron data
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'donation', 'unlimited']
