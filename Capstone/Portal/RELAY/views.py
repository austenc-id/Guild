from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
# app forms and serializers
from .forms import *
from .models import *


@login_required
def invoke(REQ):
    context = {
        'form_title': 'invoke',
        'form': InvocationForm(initial={'user': REQ.user}),
        'url': 'relay:invoke'
    }
    if REQ.POST:
        form = InvocationForm(REQ.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('portal:user_profile'))
    return render(REQ, 'forms.html', context)
