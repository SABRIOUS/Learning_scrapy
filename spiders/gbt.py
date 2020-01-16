# -*- coding: utf-8 -*-
import scrapy


class GbtSpider(scrapy.Spider):
    name = 'gbt'
    allowed_domains = ['worldpopulationreview.com/']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            name = row.xpath(".//td[1]/a/text()").get()
            gbt = row.xpath(".//td[2]/text()").get()

            yield {
                'name':name,
                'gbt':gbt
            }
