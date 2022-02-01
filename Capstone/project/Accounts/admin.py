from django.contrib import admin
from .models import *

# Displays additional Object properties in the admin panel:


class PatronAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",
                    "donation", "registered", "unlimited")


class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name")


# Register your models here:
admin.site.register(Account, AccountAdmin)
admin.site.register(Patron, PatronAdmin)
