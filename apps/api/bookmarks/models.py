from django.db import models
from django.utils import timezone

# Create your models here.

from django.conf import settings


class AuditableModelMixin(models.Model):
    updated_dt = models.DateTimeField(auto_now=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    user_cre = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_user_cre',
        default=None)
    user_upd = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='%(class)s_user_upd',
        default=None, blank=True)

    class Meta:
        abstract = True


class Tag(AuditableModelMixin):

    name = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self.name)

    class Meta:
        unique_together = ('name', 'user_cre')


class Bookmark(AuditableModelMixin):
    """ any kind of Bookmark """

    url = models.CharField(max_length=2000, default=None, null=True)
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    tags = models.ManyToManyField(Tag, related_name="bookmarks", blank=True)

    rate = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @classmethod
    def create(cls, title, description, type):
        media = cls(title=title, type=type, description=description)
        return media

    def __str__(self):
        return 'id=' + str(self.id) + ';title=' + \
            self.title + ';url=' + self.url

    class Meta:
        pass
