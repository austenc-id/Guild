from django.shortcuts import render

# Create your views here.


def index(request):
    # * Render the homepage on inital load
    return render(request, 'index.html')
