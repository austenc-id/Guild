# lib imports
from rest_framework.serializers import *

# intra-app imports
from .models import *


class PatronSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Patron
        fields = '__all__'
