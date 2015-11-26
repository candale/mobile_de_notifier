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

# File where the scraped cars will be stored
DATABASE_FILE = 'scraped_data/database.json'

# Enable or disable downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    'car_scraping.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Configure item pipelines
ITEM_PIPELINES = {
   'car_scraping.pipelines.CarScrapingPipeline': 300,
}
