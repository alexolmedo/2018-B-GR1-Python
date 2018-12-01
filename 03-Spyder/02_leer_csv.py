#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:56:33 2018

@author: usrdel
"""

import pandas as pd
import os

CSV_PATH = "/Users/usrdel/Documents/GitHub/eguez-sarzosa-vicente-adrian-python/03-Spyder/data/artwork_data.csv"


# 1) Archivos texto -> CSV JSON HTML
# 2) Binary Files
# 3) Relational Databases

data_frame_artwork = pd.read_csv(
        CSV_PATH,
        nrows=5,
        index_col= 'id',
        usecols = ['id','artist'])

columnas_a_utilizar = ['id','artist','title',
                       'medium','year',
                       'acquisitionYear','height',
                       'width','units']

data_frame_completo_artwork = pd.read_csv(
        CSV_PATH,
        index_col= 'id',
        usecols = columnas_a_utilizar)

data_frame_completo_artwork.shape


# --> Serializacion del DataFrame
# --> Deserializacion del DataFrame
# 1,2,3,4,5,6,6,7 -> DataFrame #
# DataFrameBinario -> DataFrame

PATH_GUARDADO = '/Users/usrdel/Documents/GitHub/eguez-sarzosa-vicente-adrian-python/03-Spyder/data/artwork_data_frame.pickle'
data_frame_completo_artwork.to_pickle(PATH_GUARDADO)


df_completo_pickle =pd.read_pickle(PATH_GUARDADO)


df = pd.read_excel('/Users/usrdel/Downloads/annualreferencetablesv2.xlsx', sheet_name='Births', skiprows=5)



















