# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:28:25 2018

@author: Alexander
"""

import pandas as pd
import os

df = pd.read_pickle( "C://Users//Alexander//Documents//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data_frame.pickle")


df.loc[1035,'artist']

# df.loc[0,0] # Error

df.iloc[0,1]

df.iloc[0,:]

df.iloc[0:2,0:2]

df['height']
df['width']
#df['height'] * df['width']
df_width = df['width']
dfsort_values = df['width'].sort_values()
dfsort_values_head = df['width'].sort_values().head(100)
dfsort_values_tail = df['width'].sort_values().tail(100)


a = pd.to_numeric(df['width'], errors='coerce')
b = pd.to_numeric(df['height'], errors='coerce')

df.loc[:,'width'] = a
df.iloc[:,6] = b


area = df['height'] * df['width']

df = df.assign(area=area)

dfarea=dfsort_values = df['area'].sort_values(ascending=False)
dfaream=dfsort_values = df['area'].sort_values(ascending=False).head(1)

id_max_area = df['area'].idxmax()
id_min_area = df['area'].idxmin()

el_mayor_area = df.loc[id_max_area,:]
el_menor_area = df.loc[id_min_area,:]

# Agregar una nueva serie al DF
# 1) Definir los datos como arreglo
nuevo = [99999999,'Alexander Olmedo','Pintura','Marco Lienzo Pintura',2000,2005,200,100,'mm',20000]

# 2) Definir las columnas y el ID
# list(df) No devuelve el Index
columnas = list(df)

# Agregamos la columna de Index
columnas.insert(0,'index')

#Creamos la serie
serie_nuevo = pd.Series(
        nuevo,
        index = columnas
        )

# Creamos el DF y lo transponemos
dfaux = pd.DataFrame(serie_nuevo).transpose()

# Setear el index
dfaux = dfaux.set_index('index')

# Append el nuevo dataframe
df = df.append(dfaux)

df.loc[99999999,:]



