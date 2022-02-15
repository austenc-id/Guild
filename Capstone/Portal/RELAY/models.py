from django.db.models import *
from colorful.fields import RGBColorField as ColorField
from django.contrib.auth import get_user_model

# Create your models here.


class Invocation(Model):
    user = ForeignKey(get_user_model(), on_delete=CASCADE,
                      related_name='invocations')
    title = CharField(max_length=20)
    background_color = ColorField(default='#FFFFFF')
    font_color = ColorField(default='#FFFFFF')

    def __str__(self):
        return f'{self.user} - {self.title}'
