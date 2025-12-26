import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/numerical/']

    def parse(self, response):
        for pep in response.css('tbody tr'):
            number = pep.css('a::text').get()
            name = pep.css('td + td + td a::text').get()
            link = pep.css('a::attr(href)').get()
            yield response.follow(
                link,
                callback=self.parse_pep,
                meta={'name': name, 'number': number}
            )

    def parse_pep(self, response):
        yield PepParseItem({
            'number': response.meta['number'],
            'name': response.meta['name'],
            'status': response.css('abbr::text').get(),
        })
