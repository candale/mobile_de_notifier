from __future__ import unicode_literals

from django.db import models
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

from notifications.models import SearchUrl


class Car(models.Model):
    car_id = models.CharField(max_length=1024, unique=True)
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=1024)
    price = models.CharField(max_length=50)
    seller_info = models.TextField()
    search_url = models.ForeignKey(SearchUrl, null=True, related_name='cars')
    seen = models.BooleanField(default=False)

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse(
            "admin:{}_{}_change".format(
                content_type.app_label, content_type.model),
            args=(self.id,)
        )

    def __str__(self):
        return '{} || {}'.format(self.title, self.price)


class MobileDeUrlPhoto(models.Model):
    car = models.ForeignKey('Car', related_name='photos')
    url = models.URLField(max_length=2014)
