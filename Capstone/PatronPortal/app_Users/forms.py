from django.forms import *
from .models import *
from app_Patrons.models import Patron


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

    def save(self, commit=True):
        new_user = super(Register, self).save(commit=False)
        new_user.username = self.cleaned_data['username']
        new_user.set_password(self.cleaned_data['password'])
        new_user.regcode = self.cleaned_data['regcode']
        new_user.save()
        return new_user
