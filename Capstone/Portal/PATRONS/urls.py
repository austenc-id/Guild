from django.urls import path
from .views import portal
from .viewsets import user, update, patrons, toggle

app_name = 'portal'
urlpatterns = [
    path('', portal, name='home'),
    path('register/', user.register, name='register'),
    path('login/', user.login, name='login'),
    path('logout/', user.logout, name='logout'),
    path('profile/', user.profile, name='user_profile'),
    path('update/login/', update.login, name='update_login'),
    path('update/profile/', update.profile, name='update_profile'),
    path('toggle/', toggle.favorite_color, name='toggle_color'),
    path('new/', patrons.add, name='new_patron'),
    path('view/', patrons.list, name='view_patrons'),
]
