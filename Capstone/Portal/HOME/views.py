def index(REQ):
    from django.shortcuts import render
    return render(REQ, 'index.html')
