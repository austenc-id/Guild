from django.db.models import *


# Create your models here.


class Patron(Model):
    first_name = CharField(max_length=12)
    last_name = CharField(max_length=12)
    regcode = CharField(max_length=4, unique=True)
    donation = DecimalField(default=0, max_digits=8, decimal_places=2)
    registered = BooleanField(default=False)
    unlimited = BooleanField(default=False)

    def __str__(self):
        legal_name = f'{self.first_name.title()} {self.last_name.title()}'
        return legal_name
