# -*- coding: utf-8 -*-
import logging
from urlparse import urlsplit
import re

from cars import models as django_cars_models

logger = logging.getLogger(__name__)


class CarScrapingPipeline(object):
    url_regex = re.compile("^/(?P<lang>[a-zA-Z]{,4})/[^/]+/(?P<title>[^/]+).*/(?P<id>[0-9]+\.html$)")

    def get_id_from_url(self, url):
        '''
        Expected url format:
            ...mobile.de/<lang>/Automobile/<title>/some/other/stuff/<id>.html
        '''
        url_obj = urlsplit(url)
        url_parts = url_obj.path.split('/')

        name = url_parts[2]
        id_ = url_parts[-1].strip('.html')

        return '{}::{}'.format(name, id_)

    def process_item(self, item, spider):
        car_id = self.get_id_from_url(item['url'])

        if django_cars_models.Car.objects.filter(car_id=car_id).first():
            logger.info(
                'Got item that was already processed' +
                ' (url: {}'.format(item['url'])
            )
            return

        car_obj = django_cars_models.Car.objects.create(
            car_id=car_id,
            title=item['title'],
            url=item['url'],
            price=item['price'],
            seller_info=item['seller_info']
        )

        for photo_urk in item['photos_urls']:
            django_cars_models.MobileDeUrlPhoto.objects.create(
                car=car_obj,
                url=photo_url
            )

        logger.info('Created car item with title {}'.format(item['title']))