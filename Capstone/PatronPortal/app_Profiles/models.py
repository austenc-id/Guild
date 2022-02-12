from django.db.models import *
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(Model):
    user = OneToOneField(get_user_model(), on_delete=CASCADE)
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    favorite_color = CharField(max_length=6, default='000000')

    def __str__(self):
        return self.user.username
