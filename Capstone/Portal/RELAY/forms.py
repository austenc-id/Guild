from django.forms import ModelForm, HiddenInput
from .models import Invocation


class InvocationForm(ModelForm):
    class Meta:
        model = Invocation
        fields = '__all__'
        widgets = {'user': HiddenInput()}
