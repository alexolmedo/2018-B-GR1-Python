#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:34:31 2018

@author: usrdel
"""

import numpy as np
import pandas as pd

arreglo_randomico_tres = np.random.rand(3)

arreglo_randomico_dos_dimensiones = np.random.rand(2,3)

# Pandas -> Serie

serie_arreglo = pd.Series(arreglo_randomico_tres)

serie_arreglo_v2 = pd.Series(
        arreglo_randomico_tres,
        index = ["Uno","dos","TRES"]
        )

serie_arreglo[0]
serie_arreglo_v2[0]
serie_arreglo_v2["Uno"]

serie_arreglo.index

serie_arreglo_v2.index


# DataFrames

data_frame = pd.DataFrame(arreglo_randomico_dos_dimensiones)



data_frame.columns = ['Uno','Dos','Tres']

data_frame['Uno'][0]













