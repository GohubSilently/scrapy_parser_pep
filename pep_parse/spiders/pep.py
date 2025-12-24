import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org"]

    def parse(self, response):
        for pep_link in response.css('tbody tr td a::attr(href)'):
            yield response.follow(pep_link, callback=self.pep_parse)


    def pep_parse(self, response):
        number = ''.join(response.css('ul.breadcrumbs li + li + li::text').get().replace('PEP ',''))
        name = ' '.join(response.css('h1.page-title').xpath('string(.)').get().split()[3:])
        data = {
            'number': int(number),
            'name': name,
            'status': response.css('dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)