
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import (
    get_user_model,
    logout as dj_logout,
    authenticate as auth,
    login as dj_login,
)
from django.contrib.auth.decorators import login_required
from .forms import *
from .data import *
from .models import *
# Create your views here.


def register(request):
    if request.POST:
        # verify regcode and either continue registration or display error
        regcode = request.POST['regcode']
        patron = Patron.objects.filter(regcode=regcode)
        patron = patron[0]
        # print(patron)
        if patron.registered == False:
            context = {
                'form': Verified(data={
                    'regcode': regcode,
                }),
            }
            return render(request, 'forms/verified.html', context)

        else:
            context = {
                'form': Register(),
                'error': 'not found',
            }
            return render(request, 'forms/register.html', context)

    return render(request, 'forms/register.html', {'form': Register()})
# another split??


def complete(request):
    print('request stuff', request.POST)

    if request.POST:
        # takes in form submission and registers the user if valid
        form = Verified(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            patron = Patron.objects.filter(regcode=user.regcode)
            patron = patron[0]
            user.donation = patron.donation
            if patron.unlimited:
                user.unlimited = True
            else:
                user.wallet = 1 + (user.donation // 100)
            user.save()
            patron.registered = True
            patron.save()

            return render(request, 'forms/login.html', {'message': 'registration complete', 'form': Login()})

        else:
            # invalid forms return the register template with errors
            print(form.errors.values())
            return render(request, 'forms/register.html', {'form': Register(), 'errors': form.errors.values()})


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


@login_required
def logout(user):
    # bye felicia
    dj_logout(user)
    return redirect(reverse('home:page'))


@login_required
def input(request):
    context = {
        'form': Input()
    }
    if request.POST:
        form = Input(request.POST)
        if form.is_valid():
            patron = form.save()
            patron.regcode = gen_regcode()
            patron.save()
            context.update({'message': 'input successful'})
    return render(request, 'forms/input.html', context)
