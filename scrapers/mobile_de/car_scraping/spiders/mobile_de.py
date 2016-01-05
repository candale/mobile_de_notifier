import json
import os
import urlparse
import logging

import scrapy
from scrapy import Request

import car_scraping.items as items
from car_scraping.utils import extract_text_from_html


logger = logging.getLogger(__name__)


class MobileDeSpider(scrapy.Spider):
    class Xpath:
        RESULT_PAGE_CAR_URL = "//a[@class='row vehicle-data']/@href"
        NEXT_PAGE_XPATH = "//a[contains(@class, 'pagination-nav-right')]/@href"

    name = 'mobile_de'
    allowed_domains = ["mobile.de"]

    def __init__(self):
        logger.info('Started mobile_de spider')

    def start_requests(self):
        conf_path = os.path.join(
            self.settings['BASEDIR'], self.settings['SEARCHES_URL_CONF'])
        urls_conf = json.load(open(conf_path, 'r'))
        for url in urls_conf['urls']:
            yield Request(url)

    def get_page_cars_urls(self, response):
        '''
        Gets the URL for the main page, for each car, from the main
        search results page
        '''
        car_hrefs = response.xpath(self.Xpath.RESULT_PAGE_CAR_URL)

        return [car_url.extract() for car_url in car_hrefs]

    def get_next_page_url(self, response):
        next_url = response.xpath(self.Xpath.NEXT_PAGE_XPATH)
        if not next_url:
            return None

        url = next_url[0].extract()

        return urlparse.urljoin('http://www.mobile.de', url)

    def parse(self, response):
        # Parse the main page of each car from the result page
        for car_url in self.get_page_cars_urls(response):
            yield Request(car_url, callback=self.parse_car)

        # Get the next result page and parse it
        next_url = self.get_next_page_url(response)
        if next_url:
            yield Request(next_url)

    def parse_car(self, response):
        item = items.CarItem()
        item['url'] = response.url
        item['title'] = self.get_title(response)
        item['price'] = self.get_price(response)
        item['seller_info'] = self.get_seller_info(response)
        item['photos_urls'] = self.get_photos_urls(response)

        return item

    def get_title(self, response):
        titles = response.xpath("//h1[contains(@class, 'vehicle-title')]/text()")
        if not titles:
            logger.warning(
                'Could not get page title from page {}'.format(response.url))
            return None

        return titles[0].extract()

    def get_price(self, response):
        prices = response.xpath("//p[contains(@class, 'netto-price')]/text()")

        if not prices:
            logger.warning(
                'Could not get price from page {}'.format(response.url))
            return None

        return prices[0].extract()

    def get_seller_info(self, response):
        seller_info = response.xpath("//div[contains(@class, 'seller-info')]")
        if not seller_info:
            logger.warning(
                'Could not get seller info from page {}'.format(response.url))
            return None

        return '\n'.join(
            [extract_text_from_html(info.extract()) for info in seller_info]
        )

    def get_photos_urls(self, response):
        photo_urls = response.xpath("//img[@class='slick-img']/@src")
        if not photo_urls:
            logger.warning(
                'Could not get photos from page {}'.format(response.url))
            return None

        return [photo_url.extract() for photo_url in photo_urls]
