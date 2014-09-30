import scrapy

from scrapy import Selector

from stackoverflow.items import JobItem

class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careers.stackoverflow.com"]
    start_urls = [
        "http://careers.stackoverflow.com/jobs"
    ]

    def parse(self, response):
        # <div data-jobid="68943">...</div>
        # <h3><a class="job-link" href="/jobs/69275/systems-engineer-amazon?a=5CQU76fq6s" title="Systems Engineer">Systems Engineer</a></h3>
        # <p class="tags"><a class="post-tag job-link" href="/jobs/tag/python>python</a></p>
        sel = Selector(response)
        jobs = sel.xpath('//div[@data-jobid]')
        for job in jobs:
            item = JobItem()
            item['id'] = job.xpath('.//@data-jobid')[0].extract()
            item['title'] = job.xpath('.//h3/a/text()')[0].extract()
            item['tags'] = job.css('.post-tag::text').extract()
            yield item
            

