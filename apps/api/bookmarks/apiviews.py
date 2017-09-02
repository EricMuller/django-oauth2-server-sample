from .serializers import *
from .models import *
from rest_framework import permissions
from rest_framework import generics
from rest_framework import filters
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope


class BookmarkListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['bookmarks']
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    # How to filter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)
    # required_scopes = ['music']


class TagListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['bookmarks']
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # How to filter
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('id',)
