from django.shortcuts import render
from .forms import *
# Create your views here.


def update_profile(REQ):
    context = {
        'form_title': 'update profile',
        'url': 'user_profile:update',
        'form': UpdateProfile()
    }
    return render(REQ, 'forms.html', context)


def view_profile(REQ):
    return render(REQ, 'profile.html')
