from django.urls import path
from .views import *

app_name = 'auth'
urlpatterns = [
    path('register', register, name='register'),
    path('registered', complete, name='complete'),
    path('login', login, name='login')
]
