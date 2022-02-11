# lib imports
from rest_framework.serializers import *

# intra-app imports
from .models import *


class PatronSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Patron
        # fields = ['url', 'first_name', 'last_name',
        #           'regcode', 'donation', 'unlimited', 'registered']
        fields = '__all__'
        extra_kwargs = {
            # 'url': {'view_name': 'patron-detail', 'lookup_field': 'regcode'}
        }
