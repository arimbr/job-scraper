# -*- coding: utf-8 -*-

# Scrapy settings for stackoverflow project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'stackoverflow'

SPIDER_MODULES = ['stackoverflow.spiders']
NEWSPIDER_MODULE = 'stackoverflow.spiders'
DOWNLOAD_DELAY = 0.5

MONGO_SERVER = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'stackoverflow'
MONGO_COLLECTION = 'jobs'

ITEM_PIPELINES = {
    'stackoverflow.pipelines.FormatPipeline': 100,
    'stackoverflow.pipelines.MongoDBPipeline': 200,
    'stackoverflow.pipelines.DuplicatesPipeline': 300,
    'stackoverflow.pipelines.JsonWriterPipeline': 500,
}

# Crawl responsibly by identifying yourself
# (and your website) on the user-agent
#USER_AGENT = 'stackoverflow (+http://www.yourdomain.com)'
