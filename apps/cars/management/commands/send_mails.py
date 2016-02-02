from os import path
import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.conf import settings

from notifications.models import SearchUrl
from helpers.send_mail import send_mail


class Command(BaseCommand):
    help = 'Start sending mails'

    def handle(self, *args, **options):
        searches = SearchUrl.objects.filter(
            Q(next_mailing_run_date__lte=datetime.now()) |
            Q(next_mailing_run_date=None),
            is_active=True
        )

        for search in searches:
            cars_to_send = search.cars.filter(seen=False)
            message = ''
            for car in cars_to_send:

