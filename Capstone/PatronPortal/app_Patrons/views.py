from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# app forms and serializers
from .forms import *
from .models import *
from .serializers import *
# custom utilities
from .utils import (
    generators as gen,
    extractors as extract,
)
# Create your views here.


def index(REQ):
    return render(REQ, '_patrons/index.html')


@login_required
def view_patrons(REQ):
    patrons = Patron.objects.all()
    context = {
        'patrons': patrons
    }
    serialized = PatronSerializer(patrons[0]).instance.url
    print(serialized)
    return render(REQ, '_patrons/list.html', context)


@login_required
def new_patron(REQ):
    context = {
        'form_title': 'patron input',
        'url': 'patrons:new',
        'form': NewPatron(),
    }
    if REQ.POST:
        req = REQ.POST
        keys = ['first_name', 'last_name', 'donation', 'unlimited']
        data = extract.dictionary(keys, req)
        regcode = gen.digit_code(4)
        data.update({'regcode': regcode})
        ser = PatronSerializer(data=data, context={'request': REQ})
        print(ser)
        if ser.is_valid():
            ser.save()
            return redirect(reverse('patrons:view'))
        else:
            context.update({'errors': ser.errors})
    return render(REQ, 'forms.html', context)
