# -*- coding: utf-8 -*-
import logging

from car_scraping.db.models import Car, Photo
from peewee import IntegrityError, DoesNotExist


logger = logging.getLogger(__name__)


class CarScrapingPipeline(object):

    def process_item(self, item, spider):
        # If the car already exists, don't take it again
        # We may want to update it...
        try:
            Car.get(url=item['url'])
            logger.info(
                'Got item that was already processed' +
                ' (url: {}'.format(item['url'])
            )
            return
        except DoesNotExist:
            pass

        car = Car.create(
            url=item['url'],
            price=item['price'],
            seller_info=item['seller_info'],
            title=item['title'])

        for photo in item['photos_urls']:
            Photo.create(car=car, url=photo)

        logger.info('Created car item with title {}'.format(item['title']))
