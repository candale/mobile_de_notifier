# -*- coding: utf-8 -*-
import os

from car_scraping.utils import append_to_end_of_json_list_file


class CarScrapingPipeline(object):

    def process_item(self, item, spider):
        import pudb; pu.db
        save_path = os.path.join(spider.settings['BASEDIR'],
                                 spider.settings['DATABASE_FILE'])

        append_to_end_of_json_list_file(save_path, dict(item))
