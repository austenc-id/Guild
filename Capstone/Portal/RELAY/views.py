from django.contrib.auth.decorators import login_required

@login_required
def invoke(REQ):
    from django.shortcuts import render, redirect
    from django.urls import reverse
    from .forms import InvocationForm
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
