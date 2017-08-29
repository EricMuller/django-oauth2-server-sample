from django.conf.urls import url
from user import apiviews

urlpatterns = [
    url(r'^user/$',
        apiviews.UserListView.as_view(),
        name='users'),
]
