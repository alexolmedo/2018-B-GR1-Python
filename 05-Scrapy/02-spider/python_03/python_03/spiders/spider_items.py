import scrapy
from python_03.items import ProductoItem

class SpiderItems(scrapy.Spider):

    name = 'spider_items'

    start_urls = [
        'https://www.amazon.com/s/ref=sr_ex_n_1?rh=n%3A172282%2Ck%3Amacbook&bbn=172282&keywords=macbook&ie=UTF8&qid=1547305537'
    ]

    def parse(self, response):
        lista_macbooks = response.css('ul.s-result-list > li')

        for macbook in lista_macbooks:
            titulo = macbook.css('.s-access-title::text').extract_first()
            precio = macbook.css('.a-offscreen::text').extract_first()
            link = macbook.css('a.s-access-detail-page::attr(href)').extract_first()

            titulo_truncado = titulo[:50]
            id_producto = link.split('/')[-1]
            shortened_link = 'https://www.amazon.com/dp/' + id_producto

            item_producto = ProductoItem()
            item_producto['titulo'] = titulo_truncado
            item_producto['link'] = shortened_link
            item_producto['precio'] = precio
            print(item_producto['titulo'])
            print(item_producto['link'])
            print(item_producto['precio'])

            yield item_producto

