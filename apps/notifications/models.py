from __future__ import unicode_literals
import datetime

from django.db import models


class SearchUrl(models.Model):

    class Meta:
        verbose_name = "SearchUrl"
        verbose_name_plural = "SearchUrls"

    INTERVAL_MEASURE_CHOICES = (
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks')
    )

    title = models.CharField(max_length=128)
    url = models.URLField(max_length=2048)
    subscribe_email = models.EmailField()
    update_interval = models.IntegerField()
    interval_measure = models.CharField(
        max_length=16, choices=INTERVAL_MEASURE_CHOICES)
    is_active = models.BooleanField(default=False)
    next_run_date = models.DateTimeField(null=True)
    number_of_times_scraped = models.IntegerField(default=0)

    def increment_scraped_counter(self):
        self.number_of_times_scraped += 1
        self.save()

    def save(self, *args, **kwargs):
        timedelta_kwargs = {self.interval_measure: self.update_interval}
        delta = datetime.timedelta(**timedelta_kwargs)
        self.next_run_date = datetime.datetime.now() + delta

        super(SearchUrl, self).save(*args, **kwargs)

    def __str__(self):
        return '{} | Every {} {}'.format(
            self.title, self.update_interval, self.interval_measure)
