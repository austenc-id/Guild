from email.policy import default
from django.forms import *


class User:
    class Login(ModelForm):
        # input patron data
        class Meta:
            from .models import User
            model = User
            fields = ['username', 'password']
            widgets = {'password': PasswordInput()}


    class Register(ModelForm):
        class Meta:
            from .models import User
            model = User
            fields = ['username', 'password', 'regcode']

        def save(self, commit=True, patron=False):
            from _project.utils import generate
            if patron:
                new_user = super(self.Register, self).save(commit=False)
                new_user.user_id = generate.digit_code(6)
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

class Update:
    class Login(ModelForm):
        class Meta:
            from .models import User
            model = User
            fields = ['username', 'password']
            labels = {
                'username': 'New Username',
                'password': 'New Password'
            } 
    class Profile(ModelForm):
        class Meta:
            from .models import User
            model = User
            fields = ['first_name', 'last_name', 'favorite_color', 'use_favorite_color', 'email']

class Patrons:

    class Add(ModelForm):
    # * input patron data
        class Meta:
            from .models import Patron
            model = Patron
            fields = ['first_name', 'last_name', 'donation', 'unlimited']

        def save(self, commit=True):
            from _project.utils import generate
            new_patron = super(self.NewPatron, self).save(commit=False)
            new_patron.regcode = generate.digit_code(4)
            if commit:
                new_patron.save()
            return new_patron

class Toggle:

    class FavoriteColor(ModelForm):
        class Meta:
            from .models import User
            model = User
            fields = ['use_favorite_color']
