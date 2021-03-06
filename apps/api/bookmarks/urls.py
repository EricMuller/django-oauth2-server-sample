from django.conf.urls import url
from . import apiviews

urlpatterns = [
    url(r'^bookmarks/$',
        apiviews.BookmarkListView.as_view(),
        name='bookmarks'),
    url(r'^bookmarks/(?P<pk>\d+)/$',
        apiviews.BookmarkListView.as_view(),
        name='bookmark'),
    url(r'^tags/$',
        apiviews.TagListView.as_view(),
        name='tags'),
    url(r'^tags/(?P<pk>\d+)/$',
        apiviews.TagListView.as_view(),
        name='tag'),
]
