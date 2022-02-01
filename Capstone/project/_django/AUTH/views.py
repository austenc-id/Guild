
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import (
    get_user_model,
    logout as dj_logout,
    authenticate as auth,
    login as dj_login,
)
from django.contrib.auth.decorators import login_required
from .forms import *
from .utils import generators as gen
from .models import *
# Create your views here.


def register(request):
    context = {
        'form_title': 'register',
        'form': Register(),
        'url': 'auth:register'
    }
    if request.POST:
        # verify regcode and either continue registration or display error
        regcode = request.POST['regcode']
        patron = Patron.objects.filter(regcode=regcode)
        if patron:
            patron = patron[0]
            if patron.registered == False:
                context.update({
                    'form': Verified(data={
                        'regcode': regcode,
                    }),
                    'url': 'auth:complete'

                })
                # return render(request, 'forms.html', context)

        else:
            context.update({
                'form': Register(),
                'errors': 'not found',
            })
            # return render(request, 'forms.html', context)

    return render(request, 'forms.html', context)
#! another split??


def complete(request):
    if request.POST:
        context = {

        }
        # takes in form submission and registers the user if valid
        form = Verified(request.POST)
        # ! Overide clean method of forms or save method of models
        # ! signals API?
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
                # ! could be done in the Model
            user.save()
            patron.registered = True
            patron.save()
            context.update({
                'form_title': 'login',
                'form': Login(),
                'url': 'auth:login',
                'errors': 'registration complete'
            })
            # return render(request, 'forms.html', context)

        else:
            # invalid forms return the register template with errors
            context.update({
                'form_title': 'register',
                'form': Verified(),
                'url': 'auth:complete',
                'errors': form.errors.values()

            })
        return render(request, 'forms.html', context)


def login(request):
    context = {
        'form_title': 'login',
        'form': Login(),
        'url': 'auth:login'
    }
    if request.POST:
        # takes in form submission and logs the user in if valid
        form = request.POST
        user = auth(
            request, username=form['username'], password=form['password'])
        if user != None:
            dj_login(request, user)
            return redirect(reverse('home:profile'))
        else:
            context.update({'errors': 'invalid login'})
            # return render(request, 'forms.html', context)

    return render(request, 'forms.html', context)


@login_required
def logout(user):
    # bye felicia
    dj_logout(user)
    return redirect(reverse('home:page'))


@login_required
def input_patron(request):
    context = {
        'form_title': 'input',
        'form': InputPatron(),
        'url': 'auth:input'
    }
    if request.POST:
        form = InputPatron(request.POST)
        if form.is_valid():
            patron = form.save()
            patron.regcode = gen.digit_code(4)
            patron.save()
            context.update({'errors': 'input successful'})
    return render(request, 'forms.html', context)


@login_required
def update(request):
    context = {
        'form_title': 'update',
        'form': Update(),
        'url': 'auth:update'
    }
    if request.POST:
        form = request.POST
        user = request.user
        user.display_name = form['display_name']
        user.email = form['email']
        user.phone = form['phone']
        user.save()
        return redirect(reverse('home:profile'))
    return render(request, 'forms.html', context)
