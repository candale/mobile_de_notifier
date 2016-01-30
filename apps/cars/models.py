from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    car_id = models.CharField(max_length=1024, unique=True)
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=1024)
    price = models.CharField(max_length=50)
    seller_info = models.TextField()

    def __str__(self):
        return '{} || {}'.format(self.title, self.price)


class MobileDeUrlPhoto(models.Model):
    car = models.ForeignKey('Car', related_name='photos')
    url = models.URLField(max_length=2014)
