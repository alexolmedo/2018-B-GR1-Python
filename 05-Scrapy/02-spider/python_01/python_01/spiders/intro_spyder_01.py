import scrapy

nombre_archivo = 'book_titles.csv'

class MiPrimerSpider(scrapy.Spider):
    name = 'intro_spider'
    lista_libros=[]
    lista_precios=[]
    lista_disponible=[]

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

        ## Guardar nombre: CSS y XPATH
        ## precio: CSS
        ## stock: XPATH en un archivo

        lista_libros = response.css('article > h3 > a::text').extract()
        # print (response.xpath('//article/h3/a/text()').extract())
        lista_precios = response.css('article > div.product_price > p.price_color::text').extract()
        lista_disponible = response.xpath('//article/div[2]/p[2]/i').extract()
        print (lista_libros)
        print (lista_precios)
        print (lista_disponible)

        with open(nombre_archivo, 'a+') as f:
            for index, titulo_libro in enumerate(lista_libros):
                if (lista_disponible[index]=="<i class=\"icon-ok\"></i>"):
                    disponible = '1'
                else:
                    disponible = '0'
                f.write(lista_libros[index]+ "," + lista_precios[index]+ "," + disponible+"\n")

