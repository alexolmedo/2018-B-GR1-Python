import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GenSpiderCrawl(CrawlSpider):
    name = 'follow_links_onu_02'

    start_urls = ['http://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html']

    # rules = (Rule(LinkExtractor(), callback='parse_page'),)
    rules = (Rule(LinkExtractor(
        allow='funds-programmes-specialized-agencies-and-others/index.html',
        deny=('zh/sections', 'fr/sections', 'ru/sections')
    ),callback='parse_page'),)

    def parse_page(self, response):
        lista_de_agencias = response.css('div.field-item.even > h4::text').extract()

        for agencia in lista_de_agencias:
            with open('onu_agencias.txt','a+') as archivo:
                archivo.write(agencia+"\n")
