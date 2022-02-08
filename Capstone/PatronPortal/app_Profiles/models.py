from django.db.models import *

# Create your models here.


class Profile(Model):
    legal_name = CharField(max_length=50)
    display_name = CharField(max_length=50)
    email = CharField(max_length=50)
    phone = CharField(max_length=10)
    donation = DecimalField(max_digits=8, decimal_places=2)
    tokens = IntegerField(default=1)
    unlimited = BooleanField(default=False)

    def __str__(self):
        return f'{self.legal_name}'
