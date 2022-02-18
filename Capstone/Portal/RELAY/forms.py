from django.forms import *
from .models import *


class InvocationForm(ModelForm):
    class Meta:
        model = Invocation
        fields = '__all__'
        widgets = {'user': HiddenInput()}
