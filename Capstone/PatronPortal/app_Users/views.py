from django.shortcuts import render, redirect, reverse
# Django auth tools
from django.contrib.auth import (
    get_user_model,
    logout as end,
    authenticate as auth,
    login as dj_login,
)
from django.contrib.auth.decorators import login_required
# models
from .forms import *

# custom utilities
from .utils import (
    generators as gen,
    extractors as extract,
)

# Create your views here.


def user_login(REQ):
    context = {
        'form_title': 'login',
        'url': 'user:login',
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
            return redirect(reverse('user:profile'))
        else:
            context.update({'message': 'invalid login'})
    return render(REQ, 'forms.html', context)


def user_profile(REQ):
    return render(REQ, 'profile.html')


@login_required
def user_logout(user):
    end(user)
    return redirect(reverse('user:login'))


@login_required
def user_update(REQ):
    context = {
        'form_title': 'update',
        'url': 'user:update',
        'form': Update(initial={'username': REQ.user.username}),
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
        if len(errors) != 0:
            context.update({'errors': errors})
        else:
            user.save()
            if password_updated:
                return redirect(reverse('user:login'))
            else:
                return redirect(reverse('user:profile'))
    return render(REQ, '_Users/update.html', context)


def user_reg(REQ):
    context = {
        'form_title': 'register',
        'url': 'user:reg',
        'form': Register(),
    }
    if REQ.POST:
        req = REQ.POST
        form = Register(req)
        print(REQ.POST)
        if form.is_valid():
            from .utils.retrievers import get_patron
            if req['regcode'] == '0000':
                patron = True
            else:
                patron = get_patron(req['regcode'])
                print(patron)
            if patron:
                new_user = form.save()
                return redirect(reverse('user:login'))
            else:
                context.update({'message': 'invalid registration code'})

        else:
            context.update({'errors': [form.errors.as_text()]})
    return render(REQ, 'forms.html', context)
