from django.shortcuts import render, redirect, reverse
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


@login_required
def invoke(REQ):
    context = {
        'form_title': 'invoke',
        'form': InvocationForm(initial={'user': REQ.user}),
        'url': 'relay:invoke'
    }
    if REQ.POST:
        print(REQ.POST)
        form = InvocationForm(REQ.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('portal:user_profile'))
    return render(REQ, 'forms.html', context)
