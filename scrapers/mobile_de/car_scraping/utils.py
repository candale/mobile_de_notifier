import json
import os
from HTMLParser import HTMLParser


class HtmlStripper(HTMLParser):
    '''
    http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
    '''
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def extract_text_from_html(html):
    s = HtmlStripper()
    s.feed(html)
    return s.get_data()
