from oauth2_provider.models import AbstractApplication
from django.db import models
from django.utils.translation import ugettext_lazy as _

from oauth2_provider.validators import validate_uris


class Application(AbstractApplication):

    url = models.CharField('url', max_length=200, validators=[validate_uris])

    description = models.TextField(
        blank=True
    )

    public = models.BooleanField(
        'Show it in website')

    # logo = models.ImageField(_(u'LOGO'), upload_to=utils.unique_path(
    #    'app_logo/'), storage=svmedia_storage, null=True, blank=True)

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')
        unique_together = (('client_id', 'client_secret'), )

    def __unicode__(self):
        return self.name
