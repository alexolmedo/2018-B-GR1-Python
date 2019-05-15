# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 09:19:32 2018

@author: Alexander
"""

import sqlite3
import pandas as pd

data_frame_guardado = pd.read_pickle('C://Users//Alexander//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data_frame.pickle')

seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

## SQL

with sqlite3.connect(
        'mi_base_de_datos.db') as conexion:
    seccion_df.to_sql('Artwork',conexion,if_exists='append')

## JSON

seccion_df.to_json('prueba.json')
seccion_df.to_json('prueba_tabla.json', orient='table')

## EXCEL
seccion_df.to_excel("basico.xlsx")
seccion_df.to_excel("basico_sin_indice.xlsx", index = False)  # Sin el indice
seccion_df.to_excel("solo_algunas_columnas.xlsx", columns=["artist", "title", "year"])

# Multiples hojas de trabajo
writer = pd.ExcelWriter('multiples_hojas.xlsx', engine='xlsxwriter')
seccion_df.to_excel(
        writer, 
        sheet_name = "Preview", 
        index = False)  # Hoja Preview

data_frame_guardado.to_excel(writer, sheet_name = "Complete", index = False)  # Hoja Complete todos los datos
writer.save()  # Guardar todos los archivos

## Formateo Condicional
artistas_contados = data_frame_guardado['artist'].value_counts()

artistas_contados.head()

writer = pd.ExcelWriter('colores.xlsx', engine='xlsxwriter')

artistas_contados.to_excel(writer, sheet_name='Artist Counts')

hoja = writer.sheets['Artist Counts']       

cells_range = 'B2:B{}'.format(len(artistas_contados.index))

hoja.conditional_format(cells_range,
    {
      'type':'2_color_scale',
      'min_value':'10',
      'min_type':'percentile',
      'max_value':'99',
      'max_type':'percentile'
    })
writer.save()

























