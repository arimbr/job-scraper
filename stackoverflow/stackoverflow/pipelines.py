# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem

FILE = 'items.json'


class DuplicatesPipeline(object):

    ids = []
    with open(FILE) as f:
        for line in f:
            item = json.loads(line.strip())
            ids.append(item['id'])

    def process_item(self, item, spider):
        if item['id'] in self.ids:
            raise DropItem("Item already crawled")
        else:
            return item


class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open(FILE, 'a')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
