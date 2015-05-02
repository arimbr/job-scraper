# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import datetime

from pymongo.mongo_client import MongoClient

from scrapy.exceptions import DropItem
from scrapy.conf import settings

IFILE = 'items.json'


def format_location(s):
    return s.strip()


def format_description(l):
    l = map(lambda s: s.strip(), l)
    l = filter(lambda s: s, l)
    return l  # returns a list of cleaned non empty phrases


class FormatPipeline(object):

    def process_item(self, item, spider):
        item['location'] = format_location(item['location'])
        item['description'] = format_description(item['description'])
        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings['MONGO_SERVER'],
            settings['MONGO_PORT']
        )
        db = connection.get_database(settings['MONGO_DB'])
        self.collection = db[settings['MONGO_COLLECTION']]

    def process_item(self, item, spider):
        # upsert to insert if id not found,
        # otherwise update date_updated to be now
        # date_updated will last have the last date the job was online
        date_updated = datetime.datetime.now()
        self.collection.update({'id': item['id']},
            {
                # http://docs.mongodb.org/manual/reference/operator/update/setOnInsert/
                # Both are applied for insert, only $set for update
                '$setOnInsert': dict(item),
                '$set': {'date_updated': date_updated.isoformat()}
            },
            upsert=True)
        return item


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

    def process_item(self, item, spider):
        item = dict(item)
        iline = json.dumps(item) + "\n"
        self.ifile.write(iline)
        return item
