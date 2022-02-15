from django.shortcuts import render, redirect, reverse
from django.contrib.auth import (
    authenticate as auth,
    login as dj_login,
    logout as end,
)
from django.contrib.auth.decorators import login_required
# app forms and serializers
from .forms import *
from .models import *
# custom utilities
from utils import (
    generators as gen,
    extractors as extract,
    retrievers as ret,
)
# Create your views here.


def portal(REQ):
    return render(REQ, 'portal.html')


def user_register(REQ):
    context = {
        'form_title': 'register',
        'url': 'portal:register',
        'form': Register(),
    }
    if REQ.POST:
        req = REQ.POST
        form = Register(req)
        print(REQ.POST)
        if form.is_valid():
            patron = ret.get_patron(req['regcode'])
            print(patron)
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
        req = REQ.POST
        keys = ['username', 'password']
        data = extract.dictionary(keys, req, return_list=True)
        user = auth(
            REQ, username=data[0], password=data[1])
        if user != None:
            dj_login(REQ, user)
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
        form = REQ.POST
        print(form)
        user = REQ.user
        new_username = form['new-username']
        new_password = form['new-password']
        errors = []
        if new_username != '':
            existing = User.objects.filter(username=new_username)
            if len(existing) == 0:
                user.username = new_username
            else:
                error = 'Username taken. Try again.'
                errors.append(error)
        if new_password != '':
            confirmation = form['confirm-password']
            if new_password == confirmation:
                user.set_password(new_password)
                password_updated = True
            else:
                error = 'Passwords do not match. Try again.'
                errors.append(error)
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
    patrons = Patron.objects.all().order_by('-donation')
    context = {
        'patrons': patrons
    }
    return render(REQ, 'list.html', context)


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
                context.update({'errors': ser.errors.as_text()})
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
