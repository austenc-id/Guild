from django.forms import *
from .models import *


class UpdateProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
