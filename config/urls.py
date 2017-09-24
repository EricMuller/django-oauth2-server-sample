from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include

from django.contrib import admin

from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/oauth2/', include('oauth2_application.urls')),
    url(r'^login/oauth2/', include('oauth2_provider.urls',
                                   namespace='oauth2_provider')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^about/$', AboutPageView.as_view(), name='about'),
    url(r'^api/v1/', include('api.accounts.urls', namespace='api_accounts')),
    url(r'^api/v1/', include('api.bookmarks.urls', namespace='api_bookmarks')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
