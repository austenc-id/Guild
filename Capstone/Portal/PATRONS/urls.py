from django.urls import path, include
from .views import *


app_name = 'portal'
urlpatterns = [
    path('', portal, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('update/login/', update_login, name='update_login'),
    path('update/profile/', update_profile, name='update_profile'),
    path('toggle/', toggle_color, name='toggle_color'),
    path('new/', new_patron, name='new_patron'),
    path('view/', view_patrons, name='view_patrons'),
]
