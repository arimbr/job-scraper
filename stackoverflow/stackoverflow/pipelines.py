# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem

IFILE = 'items.json'


def format_location(s):
    return s.strip()


def format_description(l):
    l = map(lambda s: s.strip(), l)
    l = filter(lambda s: s, l)
    return l  # returns a list of cleaned non empty phrases


class DuplicatesPipeline(object):

    ids = []
    with open(IFILE) as f:
        for line in f:
            item = json.loads(line.strip())
            ids.append(item['id'])

    def process_item(self, item, spider):
        if item['id'] in self.ids:
            raise DropItem("Item already crawled")
        else:
            return item


class FormatPipeline(object):

    def process_item(self, item, spider):
        item['location'] = format_location(item['location'])
        item['description'] = format_description(item['description'])
        return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.ifile = open(IFILE, 'a')

    def process_item(self, item, spider):
        item = dict(item)
        iline = json.dumps(item) + "\n"
        self.ifile.write(iline)
        return item
