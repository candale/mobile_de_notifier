# -*- coding: utf-8 -*-

import os
from os.path import dirname
import sys


# Configuration for using Django stuff

# Django project root
DJANGO_PROJECT_NAME = 'mobile_de_notifier'
DJANGO_PROJECT_ROOT = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))
sys.path.insert(0, DJANGO_PROJECT_ROOT)

# Make Django project settings available
os.environ['DJANGO_SETTINGS_MODULE'] = '{}.settings'.format(DJANGO_PROJECT_NAME)

import django
from django.conf import settings as django_settings
django.setup()


BOT_NAME = 'car_scraping'
HTTPCACHE_IGNORE_HTTP_CODES = [301, 302]

SPIDER_MODULES = ['car_scraping.spiders']
NEWSPIDER_MODULE = 'car_scraping.spiders'

BASEDIR = os.getcwd()

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = (
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
)

# File from where the search URLs are taken
SEARCHES_URL_CONF = 'conf/search_urls.json'

# Path to the database
DATABSE_FILE = django_settings.DATABSE_ABS_PATH

# Configure item pipelines
ITEM_PIPELINES = {
   'car_scraping.pipelines.CarScrapingPipeline': 300,
}

# Logger setup
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s | %(asctime)s | <%(module)s>: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logging/mobile_de.log',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'car_scraping': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'scrapy': {
            'handlers': ['console', 'file'],
            'level': 'WARNING'
        }
    }
}
