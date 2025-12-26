import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css('td a::attr(href)'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number = ''.join(response.css(
            'ul.breadcrumbs li + li + li::text'
        ).get().replace('PEP ', ''))
        name = ' '.join(response.css(
            'h1.page-title'
        ).xpath('string(.)').get().split()[3:])
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css('abbr::text').get(),
        )
