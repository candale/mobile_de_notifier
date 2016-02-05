# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_searchurl_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchurl',
            name='mail_interval_measure',
            field=models.CharField(choices=[('minutes', 'Minutes'), ('hours', 'Hours'), ('days', 'Days'), ('weeks', 'Weeks')], default='hours', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchurl',
            name='mail_sending_interval',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchurl',
            name='next_mailing_run_date',
            field=models.DateTimeField(null=True),
        ),
    ]