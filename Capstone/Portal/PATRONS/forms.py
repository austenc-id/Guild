from django.forms import *
from .models import *


class NewPatron(ModelForm):
    # * input patron data
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'donation', 'unlimited']


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

    def save(self, commit=True, testcode=None):

        new_user = super(Register, self).save(commit=False)

        new_user.username = self.cleaned_data['username']
        new_user.set_password(self.cleaned_data['password'])
        if testcode != None:
            new_user.regcode = testcode
            new_user._first_name = 'john'

        else:
            new_user.regcode = self.cleaned_data['regcode']
            new_user._first_name = 'first_name'
        if commit:
            new_user.set_user_id()
            new_user.save()
        return new_user
