from django.shortcuts import render, redirect, reverse
from django.contrib.auth import (
    get_user_model,
    logout as dj_logout,
    authenticate as auth,
    login as dj_login,
)
from .forms import *
from .data import *
# Create your views here.


def register(request):
    if request.POST:
        registrant = extract_data(request.POST)
        if registrant != 'invalid':
            patrons = get_patrons()
            verified = False
            for patron in patrons:
                patron = extract_data(patron)
                if patron[0] == registrant[0]:
                    if patron[1] == registrant[1]:
                        if patron[2] == registrant[2]:
                            verified = True
                            break
            if verified:
                context = {
                    'form': Verified(),
                    'first_name': registrant[0],
                    'last_name': registrant[1],
                    'regcode': registrant[2],

                }
                return render(request, 'forms/verified.html', context)

    return render(request, 'forms/register.html', {'form': Register()})


def login(request):
    if request.POST:
        # takes in form submission and logs the user in if valid
        form = request.POST
        user = auth(
            request, username=form['username'], password=form['password'])
        if user != None:
            dj_login(request, user)
            return redirect(reverse('home:profile'))
        else:
            return render(request, 'forms/login.html', {'form': Login(), 'message': 'invalid login'})

    return render(request, 'forms/login.html', {'form': Login()})


def complete(request):
    if request.POST:
        # takes in form submission and registers the user if valid
        form = Verified(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            patron_data = get_patron(user.regcode)
            user.wallet = 1 + (patron_data['donation'] // 100)
            user.save()
            return render(request, 'forms/login.html', {'message': 'registration complete', 'form': Login()})

        else:
            # invalid forms return the register template with errors
            return render(request, 'forms/register.html', {'form': Register(), 'errors': form.errors})
