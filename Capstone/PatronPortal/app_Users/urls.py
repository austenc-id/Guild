from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('register', user_reg, name='reg'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('profile', user_profile, name='profile'),
    path('update', user_update, name='update'),
    path('update', save_updates, name='save'),
]
