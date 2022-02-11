from rest_framework.viewsets import *
from rest_framework import permissions
from .models import Patron
from .serializers import PatronSerializer


class PatronAPIViewset(ModelViewSet):
    # ? add .order_by('field_name') method
    queryset = Patron.objects.all()
    serializer_class = PatronSerializer
    permission_classes = [permissions.IsAuthenticated]
