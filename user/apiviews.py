from django.contrib.auth.models import User
from .serializers import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope


class UserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # How to filter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # lookup_field = 'videoName' or pk

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(UserSerializer(request.user).data)
        return super(UserView, self).retrieve(request, pk)
