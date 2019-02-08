import scrapy
import csv

nombre_archivo = 'iphone.csv'


class IphoneSpider(scrapy.Spider):
    name = 'iphone_spider'
    lista_libros = []
    lista_precios = []
    lista_disponible = []

    def start_requests(self):
        urls = [
            'http://socialcompare.com/en/comparison/apple-iphone-product-line-comparison'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lista_iphone = response.css('#t > table > thead > tr > th.item::text').extract()

        lista_tamanos = response.css('#t > table > tbody > tr:nth-child(10) > td::text').extract()
        for index, item in enumerate(lista_tamanos):
            lista_tamanos[index] = item.split(' ')[0]

        lista_resolucion = response.css('#t > table > tbody > tr:nth-child(15) > td::text').extract()
        for index, item in enumerate(lista_resolucion):
            lista_resolucion[index] = item.split(' ')[0]

        lista_ram = response.css('#t > table > tbody > tr:nth-child(24) > td::text').extract()
        for index, item in enumerate(lista_ram):
            lista_ram[index] = item.split(' ')[0]
            if (float(lista_ram[index]) > 100):
                lista_ram[index] = float(lista_ram[index]) / 1000

        lista_bateria = response.css('#t > table > tbody > tr:nth-child(41) > td::text').extract()
        for index, item in enumerate(lista_bateria):
            lista_bateria[index] = item.replace('.', '')
            lista_bateria[index] = lista_bateria[index].split(' ')[0]

        lista_almacenamiento = response.css('#t > table > tbody > tr:nth-child(8) > td::text').extract()
        for index, item in enumerate(lista_almacenamiento):
            lista_almacenamiento[index] = item.split(',')[-1]
            lista_almacenamiento[index] = lista_almacenamiento[index].split('-')[-1]
            lista_almacenamiento[index] = lista_almacenamiento[index].replace('GB', '')
            lista_almacenamiento[index] = lista_almacenamiento[index].replace(' ', '')

        lista_fecha = response.css('#t > table > tbody > tr:nth-child(51) > td::text').extract()

        with open(nombre_archivo, 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(
                ['modelo',
                 'pulgadas_pantalla',
                 'resolucion_camara',
                 'ram',
                 'bateria',
                 'almacenamiento',
                 'fecha'])
            for index, titulo in enumerate(lista_iphone):
                csv_writer.writerow(
                    [lista_iphone[index],
                     lista_tamanos[index],
                     lista_resolucion[index],
                     lista_ram[index],
                     lista_bateria[index],
                     lista_almacenamiento[index],
                     lista_fecha[index]])
