from django.conf.urls import url
from . import apiviews

urlpatterns = [
    # url(r'^user/$',
    #     apiviews.UserListView.as_view(),
    #     name='users'),
    url(r'^accounts/me/$',
        apiviews.UserView.as_view()),
]
