from django.urls import path
from .views import *

app_name = 'auth'
urlpatterns = [
    path('user/register', register, name='register'),
    path('user/complete', complete, name='complete'),
    path('user/login', login, name='login'),
    path('user/logout', logout, name='logout'),
    path('user/input', input_patron, name='input'),
    path('user/update', update, name='update'),
]
