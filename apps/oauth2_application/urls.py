from __future__ import absolute_import

from django.conf.urls import url

from . import views


urlpatterns = [
    # Application management views
    url(r"^applications/register/$",
        views.ApplicationRegistration.as_view(), name="register"),
    url(r"^applications/(?P<pk>[\w-]+)/update/$",
        views.ApplicationUpdate.as_view(), name="update"),
]
