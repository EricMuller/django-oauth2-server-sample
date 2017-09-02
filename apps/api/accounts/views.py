# from django.contrib.auth.models import User
from authtools.models import User
from .serializers import *
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework.permissions import TokenHasScope


class UserView(generics.RetrieveAPIView):
    model = User
    serializer_class = BasicUserSerializer
    permission_classes = [TokenHasScope]
    required_scopes = ['profile']
    # lookup_field = 'videoName' or pk

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user:
            return Response(BasicUserSerializer(request.user).data)

        return Response(status=status.HTTP_403_FORBIDDEN)
