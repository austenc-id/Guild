def portal(REQ):
    from django.shortcuts import render, redirect
    from django.urls import reverse
    if REQ.user.is_authenticated:
        return render(REQ, 'profile.html')
    return redirect(reverse('portal:login'))
