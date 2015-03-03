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
            # job = JobItem()
            # path = sel.xpath('.//h3/a').xpath('@href')[0].extract()
            # location = sel.css('.location::text')[1].extract() \
            #               .strip().split()[1:]
            # job['id'] = sel.xpath('.//@data-jobid')[0].extract()
            # job['title'] = sel.xpath('.//h3/a/text()')[0].extract()
            # job['employer'] = sel.css('.-employer::text')[0].extract()
            # job['location'] = ' '.join(location).split(', ')
            # job['tags'] = sel.css('.post-tag::text').extract()
            # request = scrapy.Request(self.base_url + path,
            #                          callback=self.parse_job_detail_page)
            # request.meta['job'] = job
            # yield request

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
        # Store all the description elements with HTML tags
        job['description'] = response.css('.description').extract()


        # job = response.meta['job']
        # job['url'] = response.url
        # des_sel = response.xpath('//div[@class="description"]')
        # descriptions = []
        # for sel in des_sel:
        #     des = sel.xpath('.//text()').extract()
        #     des = map(lambda item: item.strip(), des)
        #     des = filter(lambda item: item, des)
        #     descriptions.append(' '.join(des))
        # job['description'] = descriptions
        # return job
        return job
