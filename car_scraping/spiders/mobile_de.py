import json
import os
import urllib
import re

import scrapy
from scrapy import Request

import car_scraping.items as items
from car_scraping.utils import extract_text_from_html


class MobileDeSpider(scrapy.Spider):
    class Xpath:
        INACTIVE_PAGE_NUMBER = ("//span[@class='pagination-page-number']//a")
        ACTIVR_PAGE_NUMBER = (
            "//span[@class='pagination-page-number']//span[@class='active']")
        RESULT_PAGE_CAR_URL = (
            "//a[starts-with(@id, 'entryVehicle')]/@href")

    URL_PAGE_NUMBER_REGEX = re.compile('(?P<page_id>pgn)(?P<sep>:)(?P<page_number>\d+)')

    name = 'mobile_de'
    allowed_domains = ["mobile.de"]

    def __init__(self):
        self.number_of_result_pages = None

    def start_requests(self):
        conf_path = os.path.join(
            self.settings['BASEDIR'], self.settings['SEARCHES_URL_CONF'])
        urls_conf = json.load(open(conf_path, 'r'))
        for url in urls_conf['urls']:
            yield Request(url)

    def get_page_number_from_url(self, url):
        page_str_search = self.URL_PAGE_NUMBER_REGEX.search(url)
        if page_str_search:
            page_number = page_str_search.group('page_number')
            return int(page_number)

        return None

    def get_next_page_url(self, current_url):
        '''
        The pagination in for mobile.de is contained as parameter in the
        URL under the from
            ...,param1:x,pgn:page_number,param2:y,...
        All we need to do is replace pgn with the next number
        '''
        current_page = self.get_page_number_from_url(current_url)
        if current_page == self.number_of_result_pages:
            return None

        # this might be overkill
        sub_regex = "\g<page_id>\g<sep>{}".format(current_page + 1)
        return self.URL_PAGE_NUMBER_REGEX.sub(sub_regex, current_url)

    def get_page_cars_urls(self, response):
        '''
        Gets the URL for the main page, for each car, from the main
        search results page
        '''
        car_hrefs = response.xpath(self.Xpath.RESULT_PAGE_CAR_URL)

        return [car_url.extract() for car_url in car_hrefs]

    def get_number_of_result_pages(self, response):
        number_of_inactive_pages = len(
            response.xpath(self.Xpath.INACTIVE_PAGE_NUMBER)
        )
        active_page = len(response.xpath(self.Xpath.ACTIVR_PAGE_NUMBER))

        return number_of_inactive_pages + active_page

    def parse(self, response):
        # Get the number of result pages
        if self.number_of_result_pages is None:
            self.number_of_result_pages = (
                self.get_number_of_result_pages(response))

        # Parse the main page of each car from the result page
        for car_url in self.get_page_cars_urls(response):
            yield Request(car_url, callback=self.parse_car)

        # Get the next result page and parse it
        next_url = self.get_next_page_url(response.url)
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
        return titles[0].extract() if titles else None

    def get_price(self, response):
        prices = response.xpath("//p[contains(@class, 'locale-price')]/text()")
        return prices[0].extract() if prices else None

    def get_seller_info(self, response):
        seller_info = response.xpath("//div[contains(@class, 'seller-info')]")
        return '\n'.join(
            [extract_text_from_html(info.extract()) for info in seller_info]
        )

    def get_photos_urls(self, response):
        photo_urls = response.xpath("//img[@class='slick-img']/@src")
        return [photo_url.extract() for photo_url in photo_urls]
