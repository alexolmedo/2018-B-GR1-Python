# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import pandas as pd
import os
import numpy

data_frame_guardado = pd.read_pickle('C://Users//Alexander//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data_frame.pickle')

seccion_df = data_frame_guardado.iloc[49980:50019,:].copy()

# group by

df_agrupado = seccion_df.groupby('acquisitionYear')

type(df_agrupado)

for anio, data_frame_agrupado_de_artista in df_agrupado:
    print('Año:{}'.format(anio))
    print(data_frame_agrupado_de_artista)
    #anio_minimo = data_frame_agrupado_de_artista['acquisitionYear'].min()
	#print(type(data_frame_agrupado_de_artista))
	#print("{}:{}".format(name,anio_minimo))
    
    
def llenar_valores_vacios(series):
    valores_contados = series.value_counts()
    if valores_contados.empty:
        return series
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        if type(valor)==str:
            sumatoria += int(valor)
        if type(valor)==float:
            numero_nans += 1
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    return valor_mas_utilizado

def transformar_df_por_artista(df):
    agrupado_por_artista = df.groupby('artist')
    for nombre_artista, grupo in agrupado_por_artista:
        df_llenado = grupo.copy()
        #print(grupo['height']) # Devuelve una serie
        df_llenado.loc[:,'height'] = llenar_valores_vacios(grupo['height'])
        #print(df_llenado)
        
transformar_df_por_artista(seccion_df)
        
