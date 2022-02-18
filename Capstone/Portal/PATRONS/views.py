from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (authenticate as auth, login as login, logout as end)
from django.contrib.auth.decorators import login_required
# app forms and serializers
from .forms import *
from .models import *
# custom utilities
from utils.extractors import *
from utils.retrievers import *


def portal(REQ):
    if REQ.user.is_authenticated:
        return render(REQ, 'profile.html')
    return redirect(reverse('portal:login'))


def user_register(REQ):
    context = {
        'form_title': 'register',
        'url': 'portal:register',
        'form': Register(),
    }
    if REQ.POST:
        form = Register(REQ.POST)
        if form.is_valid():
            patron = get_patron(REQ.POST['regcode'])
            if patron:
                new_user = form.save(patron=patron)
                return redirect(reverse('portal:login'))
            else:
                context.update({'message': 'invalid registration code'})
        else:
            context.update({'errors': [form.errors.as_text()]})
    return render(REQ, 'forms.html', context)


def user_login(REQ):
    context = {
        'form_title': 'login',
        'url': 'portal:login',
        'form': Login()
    }
    if REQ.POST:
        # takes in form submission and logs the user in if valid
        keys = ['username', 'password']
        data = dictionary(keys, REQ.POST, return_list=True)
        user = auth(
            REQ, username=data[0], password=data[1]
            )
        if user != None:
            login(REQ, user)
            user.login_count += 1
            user.save()
            return redirect(reverse('portal:user_profile'))
        else:
            context.update({'message': 'invalid login'})
    return render(REQ, 'forms.html', context)


@login_required
def update_login(REQ):
    context = {
        'form_title': 'update',
        'url': 'portal:update_login',
        'form': UpdateLogin(initial={'username': REQ.user.username}),
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
def user_logout(user):
    end(user)
    return redirect(reverse('portal:login'))


@login_required
def user_profile(REQ):
    user = REQ.user
    if user.confirm_profile:
        user.confirm_profile = False
        user.save()
        return redirect(reverse('portal:update_profile'))
    return render(REQ, 'profile.html')


@login_required
def update_profile(REQ):
    user = REQ.user
    context = {
        'form_title': 'update profile',
        'url': 'portal:update_profile',
        'form': UpdateProfile(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'favorite_color': user.favorite_color,
            'use_favorite_color': user.use_favorite_color,
            'email': user.email})
    }
    if REQ.POST:
        form = UpdateProfile(REQ.POST, instance=REQ.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('portal:user_profile'))
        else:
            context.update({'errors': form.errors.as_text()})
    return render(REQ, 'forms.html', context)


@login_required
def view_patrons(REQ):
    return render(REQ, 'list.html', {'patrons': Patron.objects.all().order_by('-donation')})


@login_required
def new_patron(REQ):
    if REQ.user.is_superuser:
        context = {
            'form_title': 'patron input',
            'url': 'portal:new_patron',
            'form': NewPatron(),
        }
        if REQ.POST:
            form = NewPatron(REQ.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse('portal:view_patrons'))
            else:
                context.update()
        return render(REQ, 'forms.html', context)
    return redirect(reverse('portal:home'))


def toggle_color(REQ):
    context = {
        'form_title': 'toggle favorite color',
        'url': 'portal:toggle_color',
        'form': ToggleFavoriteColor(initial={'use_favorite_color': REQ.user.use_favorite_color}),
    }
    if REQ.POST:
        form = ToggleFavoriteColor(REQ.POST, instance=REQ.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('portal:user_profile'))
    return render(REQ, 'forms.html', context)
