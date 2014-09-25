import scrapy

from stackoverflow.items import JobItem

class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careers.stackoverflow.com"]
    start_urls = [
        "http://careers.stackoverflow.com/jobs"
    ]

    def parse(self, response):
        # <div data-jobid="68943">...</div>
        jobs = response.css('div::attr(data-jobid)')
        for job in jobs:
            item = JobItem()
            item['id'] = job.extract()
            yield item
            

