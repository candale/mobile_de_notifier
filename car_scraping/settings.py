# -*- coding: utf-8 -*-

import os

BOT_NAME = 'car_scraping'

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
DATABSE_FILE = 'db/cars.db'

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
            'level': 'INFO',
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
        }
    }
}
