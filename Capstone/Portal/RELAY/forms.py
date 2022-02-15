from django.forms import *


from utils import (
    generators as gen,
    extractors as extract,
    retrievers as ret,
)
from .models import *


class InvocationForm(ModelForm):
    class Meta:
        model = Invocation
        fields = '__all__'
        widgets = {'user': HiddenInput()}
