from django.conf.urls import url
from user import apiviews

urlpatterns = [
    url(r'^user/$',
        apiviews.UserListView.as_view(),
        name='users'),
    url(r'^user/(?P<pk>[^/]+)/$',
        apiviews.UserView.as_view(),
        name='user'),
]
