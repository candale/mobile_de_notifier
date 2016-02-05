from os import path
import datetime

from django.utils import timezone
from django.core.management.base import BaseCommand
from django.db.models import Q
from django.conf import settings

from notifications.models import SearchUrl
from helpers.send_email import send_email


class Command(BaseCommand):
    help = 'Start sending mails'

    def handle(self, *args, **options):
        searches = SearchUrl.objects.filter(
            Q(next_mailing_run_date__lte=timezone.now()) |
            Q(next_mailing_run_date=None),
            is_active=True
        )

        for search in searches:
            cars_to_send = search.cars.filter(seen=False)

            if cars_to_send.count() == 0:
                continue

            html = '''
            <html>
                <h1>Search title: {}</h1>
                <h2>Url: <a href="{}">link</a></h2>
                <h3>Cars</h3>
            '''.format(search.title, search.url)

            for car in cars_to_send:
                car_info = '''
                    <strong>Title:</strong>{}<br>
                    <strong>Price:</strong>{}<br>
                    <strong>Url:</strong>{}<br>
                '''.format(car.title, car.price, car.url)

                car_imgs_html = ''
                for img in car.photos.all():
                    car_imgs_html += '<img src="{}">'.format(img.url)

                html += car_info
                html += car_imgs_html

                html += '<hr>'

                car.seen = True
                car.save()

            html += '</html>'

            subject = 'New results for custom search | {}'.format(search.title)
            send_email(
                settings.MAIL_ADDRESS, settings.MAIL_PASSWORD,
                search.subscribe_email, subject, html)

            search.increment_emails_sent()
