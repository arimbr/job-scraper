# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.exceptions import DropItem

IFILE = 'items.json'
DFILE = 'descriptions.json'


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


class JsonWriterPipeline(object):

    def __init__(self):
        self.ifile = open(IFILE, 'a')
        self.dfile = open(DFILE, 'a')

    def process_item(self, item, spider):
        item = dict(item)
        # dline = json.dumps({"id": item["id"],
        #                     "description": item.pop("description")}) + "\n"
        iline = json.dumps(item) + "\n"
        # self.dfile.write(dline)
        self.ifile.write(iline)
        return item
