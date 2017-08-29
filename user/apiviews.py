from django.contrib.auth.models import User
from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope


class UserListView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # How to filter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)
