import datetime

import scrapy

from stackoverflow.items import JobItem


class JobSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["careers.stackoverflow.com"]
    start_time = datetime.datetime.now()

    def start_requests(self):
        for i in xrange(1, 100):
            yield self.make_requests_from_url(
                "http://careers.stackoverflow.com/jobs/?pg=%d" % i)

    def parse(self, response):
        """
        Get job id, date, title, employer, location, tags
        Returns request object with job data
        """
        jobs = response.xpath('//div[@data-jobid]')

        for sel in jobs:
            job = JobItem()
            jobid = sel.xpath('.//@data-jobid')[0].extract()
            location = sel.css('.location::text')[1].extract() \
                          .strip().split()[1:]
            job['id'] = jobid
            job['date'] = self.start_time.isoformat()
            job['title'] = sel.xpath('.//h3/a/text()')[0].extract()
            job['employer'] = sel.css('.-employer::text')[0].extract()
            job['location'] = ' '.join(location).split(', ')
            job['tags'] = sel.css('.post-tag::text').extract()
            request = scrapy.Request("http://careers.stackoverflow.com/jobs/" +
                                     jobid,
                                     callback=self.parse_job_detail_page)
            request.meta['job'] = job
            yield request

    def parse_job_detail_page(self, response):
        """
        Get job url, description
        Returns job item to pipeline
        """
        job = response.meta['job']
        job['url'] = response.url
        des_sel = response.xpath('//div[@class="description"]')
        description = []
        for sel in des_sel:
            des_text = sel.xpath('.//text()').extract()
            des_list = filter(lambda item: item.strip(), des_text)
            description.append(' '.join(des_list))
        job['description'] = description
        return job
