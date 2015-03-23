import datetime

import scrapy
from scrapy import log

from stackoverflow.items import JobItem


class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careers.stackoverflow.com"]
    base_url = "http://careers.stackoverflow.com"
    job_base_url = "http://careers.stackoverflow.com/jobs/"
    start_time = datetime.datetime.now()

    def start_requests(self):
        for i in xrange(1, 100):
            yield self.make_requests_from_url(
                "http://careers.stackoverflow.com/jobs/?pg=%d" % i)

    def parse(self, response):
        """
        Get job id
        Returns request object for job url
        """
        # looks for <a> elements with a data-jobid attribute
        # <a class="fav-toggle" data-jobid="81955"
        # href="/jobs/togglefavorite/81955?returnUrl=%2fjobs"></a>
        jobs_id = response.css('a').xpath('@data-jobid').extract()

        # Yield a request object to the job detail page
        for job_id in jobs_id:
            job = JobItem()
            job['id'] = job_id
            job_url = self.job_base_url + job_id
            request = scrapy.Request(job_url,
                                     callback=self.parse_job_detail_page)
            request.meta['job'] = job
            yield request

    def parse_job_detail_page(self, response):
        """
        Get job url, date, title, employer, tags, location and description
        Returns job item to pipeline
        """
        #log.msg("We got a request to: " + response.url)
        job = response.meta['job']
        job['url'] = response.url
        job['date'] = self.start_time.isoformat()
        job['title'] = response.css('#hed h1 a::text')[0].extract()
        job['employer'] = response.css('#hed .employer::text')[0].extract()
        job['tags'] = response.css('#hed .tags a::text').extract()
        job['location'] = response.css('#hed .location::text')[0].extract()
        # Use xpath selectors and //text() for getting all the text in different levels
        job['description'] = response.xpath('//div[@class="description"]//text()').extract()

        return job
