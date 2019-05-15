# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 08:08:18 2018

@author: Alexander
"""

import pandas as pd
import dateutil

# Cargar datos csv
data = pd.read_csv('https://shanelynnwebsite-mid9n9g1q9y8tt.netdna-ssl.com/wp-content/uploads/2015/06/phone_data.csv')

# Convertir string de fecha a datetime
data['date'] = data['date'].apply(dateutil.parser.parse, dayfirst=True)

# Meses únicos en los que se agrupó
data.groupby(['month']).groups.keys()

# Suma de la duración total de las llamadas, por mes
duracion_mes = data.groupby('month')['duration'].sum()

# Suma de número de registros totales, por mesw
registros_mes = data.groupby('month')['date'].count()

# Duraciones total de llamadas, según la operadora
llamadas_operadoras = data[data['item'] == 'call'].groupby('network')['duration'].sum()

# Número de llamadas, sms y datos, agrupados por mes
print(data.groupby(['month', 'item'])['date'].count())

# Llamadas a cada operadora, agrupadas por mes
print(data.groupby(['month', 'network'])['date'].count())

# Múltiples estadísticas
print(data.groupby(['month', 'item']).agg(
        {
            'duration':sum,
            'item': "count"
         }
        ))  