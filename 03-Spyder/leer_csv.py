# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 10:04:09 2018

@author: Alexander
"""
import pandas as pd
import os 

CSV_PATH ="C://Users//Alexander//Documents//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data.csv"

# 1) Archivos texto
# 2) Binary Files

data_frame_artwork = pd.read_csv(
        CSV_PATH,
        nrows=5,
        index_col= 'id',
        usecols=['id','artist'])

columnas_a_utilizar = ['id','artist','title',
                       'medium','year',
                       'acquisitionYear','height',
                       'width','units']

data_frame_completo_artwork = pd.read_csv(
        CSV_PATH,
        index_col= 'id',
        usecols=columnas_a_utilizar)

data_frame_completo_artwork.shape

# --> Serialización del DataFrame
# --> Deserialización del DataFrame
PATH_GUARDADO ="C://Users//Alexander//Documents//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data_frame.pickle"
data_frame_completo_artwork.to_pickle(PATH_GUARDADO)
df = pd.read_pickle(PATH_GUARDADO)
