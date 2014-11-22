import datetime

import scrapy

from stackoverflow.items import JobItem


class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careers.stackoverflow.com"]
    start_time = datetime.datetime.now()

    def start_requests(self):
        for i in xrange(1, 2):
            yield self.make_requests_from_url(
                "http://careers.stackoverflow.com/jobs/?pg=%d" % i)

    def parse(self, response):
        # Get job id, title, tags, date, location, employer, url
        # Make request to job detail url

        jobs = response.xpath('//div[@data-jobid]')

        for sel in jobs:
            job = JobItem()
            jobid = sel.xpath('.//@data-jobid')[0].extract()
            job['id'] = jobid
            job['title'] = sel.xpath('.//h3/a/text()')[0].extract()
            job['tags'] = sel.css('.post-tag::text').extract()
            job['date'] = str(self.start_time)
            request = scrapy.Request("http://careers.stackoverflow.com/jobs/" +
                                     jobid,
                                     callback=self.parse_job_detail_page)
            request.meta['job'] = job
            yield request

    def parse_job_detail_page(self, response):
        # Get job description
        job = response.meta['job']
        job['url'] = response.url
        return job
