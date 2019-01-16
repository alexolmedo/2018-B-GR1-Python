# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ValidarMacbook(object):
    def process_item(self, item, spider):
        if ('macbook' not in item['titulo'].lower() or float(item['precio'].replace('$','').replace(',','')) < 200.0):
            item['titulo'] = 'No-Macbook'
        return item

class ValidarPrecio(object):
    def process_item(self, item, spider):
        precio = float(item['precio'].replace('$','').replace(',',''))
        if (precio < 900.0):
            item['precio'] = 'Muy Barato'
        return item

# class MarkarComoViable(object):
#   def process_item(self, item, spider):
#     if item['titulo'] != 'No-Macbook' and item['precio'] != 'Inasequible':
#       print("\n \nItem encontrado")
#       print("Titulo", item['titulo'])
#       print("Precio", item['precio'])
#       print("Link", item['link'])
#       print("\n")
#     return item
