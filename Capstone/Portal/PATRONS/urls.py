from django.urls import path, include
from .views import *


app_name = 'portal'
urlpatterns = [
    path('', portal, name='home'),
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('login/update', update_login, name='update_login'),
    path('logout', user_logout, name='logout'),
    path('patrons/new', new_patron, name='new_patron'),
    path('patrons/view', view_patrons, name='view_patrons'),
    path('patrons/profile/', user_profile, name='user_profile'),
    path('patrons/profile/update', update_profile, name='update_profile'),
]
