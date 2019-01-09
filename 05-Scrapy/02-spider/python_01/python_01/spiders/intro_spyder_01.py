import scrapy

nombre_archivo = 'book_titles.txt'

class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider'

    def start_requests(self):  ## self = this
        urls = [
            'http://books.toscrape.com/catalogue/page-1.html',
            'http://books.toscrape.com/catalogue/page-2.html',
            'http://books.toscrape.com/catalogue/page-3.html',
            'http://books.toscrape.com/catalogue/page-4.html',
            'http://books.toscrape.com/catalogue/page-5.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print (response.css('article > h3 > a::text').extract())
        #print (response.xpath('//article/h3/a/text()').extract())
        lista_libros = response.css('title::text').extract()
