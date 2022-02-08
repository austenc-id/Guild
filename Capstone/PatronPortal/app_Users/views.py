from django.shortcuts import render, redirect, reverse
# Django auth tools
from django.contrib.auth import (
    get_user_model,
    logout as end,
    authenticate as auth,
    login as dj_login,
)
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


def user_logout():
    return


def user_reg():
    return
