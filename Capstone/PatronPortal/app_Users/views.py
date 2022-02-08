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
        'form': Update(),
    }
    if REQ.POST:
        form = REQ.POST
        try:
            form['username']
            new_username = True
        except:
            new_username = False
        try:
            form['password']
            new_password = True
        except:
            new_password = False
        context.update({
            'new_username': new_username,
            'new_password': new_password,
            # ! URL is not updating??
            'url': 'user:save'
        })
    return render(REQ, '_Users/update.html', context)


@login_required
def save_updates(REQ):
    return


def user_reg():
    return
