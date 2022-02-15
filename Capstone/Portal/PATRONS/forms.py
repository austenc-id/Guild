from django.forms import *
from utils import (
    generators as gen,
    extractors as extract,
    retrievers as ret,
)
from .models import *


class NewPatron(ModelForm):
    # * input patron data
    class Meta:
        model = Patron
        fields = ['first_name', 'last_name', 'donation', 'unlimited']

    def save(self, commit=True):
        new_patron = super(NewPatron, self).save(commit=False)
        new_patron.regcode = gen.digit_code(4)
        if commit:
            new_patron.save()
        return new_patron


class Login(ModelForm):
    # input patron data
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': PasswordInput()}


class UpdateLogin(ModelForm):
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

    def save(self, commit=True, patron=False):
        if patron:
            new_user = super(Register, self).save(commit=False)
            new_user.user_id = gen.digit_code(6)
            new_user.username = self.cleaned_data['username']
            new_user.set_password(self.cleaned_data['password'])
            new_user.regcode = self.cleaned_data['regcode']
            new_user.first_name = patron.first_name
            new_user.last_name = patron.last_name
            new_user.donation = patron.donation
            new_user.tokens = 1 + (patron.donation // 25)
            try:
                new_user.email = patron.email
            except:
                pass
            if commit:
                new_user.save()
                patron.registered = True
                patron.save()
            return new_user
        return None


class UpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'favorite_color', 'use_favorite_color', 'email']


class ToggleFavoriteColor(ModelForm):
    class Meta:
        model = User
        fields = ['use_favorite_color']
