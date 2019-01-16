import scrapy
from scrapy.loader.processors import MapCompose
# Apply a sequence of functions to any list

def shorten_amazon_link(link):
  id_producto = link.split('/')[-1]  # ultimo elemento
  short_link = 'https://www.amazon.com/dp/' + id_producto
  return short_link

class ItemProducto(scrapy.Item):
  titulo = scrapy.Field()
  precio = scrapy.Field()
  link = scrapy.Field(
     input_processor = MapCompose(shorten_amazon_link)
  )