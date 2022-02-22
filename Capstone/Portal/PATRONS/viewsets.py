from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (authenticate as auth, login as djlogin, logout as end)
from django.contrib.auth.decorators import login_required


class user:
    def register(REQ):
        """
        GET: renders the registration form

        POST: creates a new user object and redirects to the login page or rerenders the form with errors
        """
        from _project.utils import retrieve
        from .forms import User
        context = {
            'form_title': 'register',
            'url': 'portal:register',
            'form': User.Register(),
        }
        if REQ.POST:
            form = User.Register(REQ.POST)
            if form.is_valid():
                patron = retrieve.patron(regcode=REQ.POST['regcode'])
                if patron:
                    new_user = form.save(patron=patron)
                    return redirect(reverse('portal:login'))
                else:
                    context.update({'message': 'invalid registration code'})
            else:
                context.update({'errors': [form.errors.as_text()]})
        return render(REQ, 'forms.html', context)

    def login(REQ):
        """
        GET: renders the login form

        POST: sets the request user and redirects to the user's profile page or rerenders the form with errors
        """
        from .forms import User
        from _project.utils import extract
        context = {
            'form_title': 'login',
            'url': 'portal:login',
            'form': User.Login()
        }
        if REQ.POST:
            # takes in form submission and logs the user in if valid
            keys = ['username', 'password']
            data = extract.request_data(keys, REQ.POST, return_list=True)
            user = auth(
                REQ, username=data[0], password=data[1]
                )
            if user != None:
                djlogin(REQ, user)
                user.login_count += 1
                user.save()
                return redirect(reverse('portal:user_profile'))
            else:
                context.update({'message': 'invalid login'})
        return render(REQ, 'forms.html', context)

    @login_required
    def logout(user):
        """
        GET: removes the request user and redirects to the login page
        """
        end(user)
        return redirect(reverse('portal:login'))

    @login_required
    def profile(REQ):
        """
        GET: renders the user's profile unless flagged to confirm profile details where it will redirect to the 'portal:update_profile'
        """
        user = REQ.user
        if user.confirm_profile:
            user.confirm_profile = False
            user.save()
            return redirect(reverse('portal:update_profile'))
        return render(REQ, 'profile.html')

class update:
    @login_required
    def login(REQ):
        """
        GET: renders the update login form

        POST: sets the user's username and/password and redirects to either the login page or the user's profile page or rerenders the form with errors
        """
        from .forms import Update
        from .models import User
        context = {
            'form_title': 'update login',
            'url': 'portal:update_login',
            'form': Update.Login(initial={'username': REQ.user.username}),
        }
        if REQ.POST:
            user = REQ.user
            new_username = REQ.POST['new-username']
            new_password = REQ.POST['new-password']
            errors = []
            if new_username != '':
                existing = User.objects.filter(username=new_username)
                if len(existing) == 0:
                    user.username = new_username
                else:
                    errors.append('Username taken. Try again.')
            if new_password != '':
                confirmation = REQ.POST['confirm-password']
                if new_password == confirmation:
                    user.set_password(new_password)
                    password_updated = True
                else:
                    errors.append('Passwords do not match. Try again.')
            else:
                password_updated = False
            if len(errors) != 0:
                context.update({'errors': errors})
            else:
                user.save()
                if password_updated:
                    return redirect(reverse('portal:login'))
                else:
                    return redirect(reverse('portal:user_profile'))
        return render(REQ, 'update/login.html', context)
    
    @login_required
    def profile(REQ):
        """
        GET: renders the user's profile as a form to update details

        POST: saves the user's profile and redirect to the user's profile or rerenders the form with errors
        """
        from .forms import Update
        user = REQ.user
        context = {
            'form_title': 'update profile',
            'url': 'portal:update_profile',
            'form': Update.Profile(initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'favorite_color': user.favorite_color,
                'use_favorite_color': user.use_favorite_color,
                'email': user.email})
        }
        if REQ.POST:
            form = Update.Profile(REQ.POST, instance=REQ.user)
            if form.is_valid():
                form.save()
                return redirect(reverse('portal:user_profile'))
            else:
                context.update({'errors': form.errors.as_text()})
        return render(REQ, 'forms.html', context)

class patrons:
    @login_required
    def list(REQ):
        """Renders a list of all patrons in the db ordered by donation amount."""
        from .models import Patron
        return render(REQ, 'list.html', {'patrons': Patron.objects.all().order_by('-donation')})
    
    @login_required
    def add(REQ):
        """
        GET: if the user has permissions render the new patron form or redirects home if they do not
        
        POST: creates a new patron object and redirects to the patron list page or rerenders the form with errors.
        """
        from .forms import Patrons
        if REQ.user.is_superuser:
            context = {
                'form_title': 'patron input',
                'url': 'portal:new_patron',
                'form': Patrons.Add(),
            }
            if REQ.POST:
                form = Patrons.Add(REQ.POST)
                if form.is_valid():
                    form.save()
                    return redirect(reverse('portal:view_patrons'))
                else:
                    context.update()
            return render(REQ, 'forms.html', context)
        return redirect(reverse('portal:home'))

class toggle:
    @login_required
    def favorite_color(REQ):
        """
        GET: renders a form to update user.use_favorite_color

        POST: saves the changes then redirects to the user's profile
        """
        from .forms import Toggle
        context = {
            'form_title': 'toggle favorite color',
            'url': 'portal:toggle_color',
            'form': Toggle.FavoriteColor(initial={'use_favorite_color': REQ.user.use_favorite_color}),
        }
        if REQ.POST:
            form = Toggle.FavoriteColor(REQ.POST, instance=REQ.user)
            if form.is_valid():
                form.save()
            return redirect(reverse('portal:user_profile'))
        return render(REQ, 'forms.html', context)