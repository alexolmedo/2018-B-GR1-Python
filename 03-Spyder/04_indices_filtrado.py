# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:47:00 2018

@author: USRSIG
"""
import pandas as pd
import os

directorio_archivo = "C://Users//USRSIG//Documents//GitHub//eguez-sarzosa-vicente-adrian//03-Spyder//data//artwork_data_frame.pickle"

df_guardado = pd.read_pickle(directorio_archivo)


artistas_df_duplicados = df_guardado["artist"]

artistas_df = pd.unique(artistas_df_duplicados)

len(artistas_df)  # 3336

artistas_bacon_francis = df_guardado["artist"] == 'Bacon, Francis'


# Valores y cuantos tenemos de ese tipo de valor

artistas_bacon_francis.value_counts()


# otra forma

serie_artistas = df_guardado['artist'].value_counts()

serie_artistas['Bacon, Francis']









