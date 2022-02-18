from django.shortcuts import render


def index(REQ):
    # * Render the homepage on inital load
    return render(REQ, 'index.html')
