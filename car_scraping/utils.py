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


def append_to_end_of_json_list_file(path, data, create_if_not_exists=False):
    '''
    Appends a new dictionary to the end of a JSON file
    that has as its first level a list
    [
        ...
    ]
    '''
    existed = True
    if not os.path.exists(path):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError:
            pass

        f = open(path, "w")
        f.write("[]")
        existed = False

    f = open(path, 'r+')
    f.seek(-1, 2)
    f.write("{}\n{}]".format(
            "," if existed else "",
            unicode(json.dumps(data, ensure_ascii=False, encoding='utf8'))
        )
    )
    f.close()
