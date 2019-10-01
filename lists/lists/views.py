from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Record, List
from .serializers import UserSerializer, GroupSerializer, RecordSerializer, ListSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()  # .order_by('list.owner')
    serializer_class = RecordSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
