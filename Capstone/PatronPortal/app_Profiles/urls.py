from django.urls import path
from .views import *

app_name = 'user_profile'
urlpatterns = [
    path('', view_profile, name='view'),
    path('update', update_profile, name='update'),
]
