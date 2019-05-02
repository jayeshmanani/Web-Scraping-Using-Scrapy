# -*- coding: utf-8 -*-
import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.mumbai.craigslist.org']
    start_urls = ['https://mumbai.craigslist.org/search/eve']

    def parse(self, response):
        print('Extracting…' + response.url)

        titles = response.css('a.result-title::text').getall()
        result = dict()

        for sr_no, title in enumerate(titles):
        	print(sr_no, title)
        	result['Sr_no'] = sr_no
        	result['Title'] = title
	        yield result
