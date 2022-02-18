from django.db.models import *
from django.utils.text import format_lazy
from colorful.fields import RGBColorField as ColorField
from django.contrib.auth import get_user_model
from utils.retrievers import *


class Invocation(Model):
    user = ForeignKey(get_user_model(), on_delete=CASCADE, related_name='invocations')
    title = CharField(max_length=20)
    purpose = CharField(default='', max_length=25, choices=[('Blog', 'share my opinions'), ('Org', 'promote my organization'), ('Shop', 'sell my goods and/or services')])
    background_color = ColorField(default='#FFFFFF')
    card_background_color = ColorField(default='#FFFFFF')
    border_color = ColorField(default='#FFFFFF')
    font_color = ColorField(default='#FFFFFF')
    link_color = ColorField(default='#FFFFFF')
    primary_font = CharField(choices=get_google_fonts(), max_length=99, default='', help_text='visit https://fonts.google.com/ to browse')

    def __str__(self):
        return f'{self.user} - {self.title}'
