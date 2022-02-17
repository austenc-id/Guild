from django.shortcuts import render

# Create your views here.


def index(REQ):
    # * Render the homepage on inital load
    return render(REQ, 'index.html')
