import scrapy

class ItemProducto(scrapy.Item):
  titulo = scrapy.Field()
  precio = scrapy.Field()
  link = scrapy.Field()