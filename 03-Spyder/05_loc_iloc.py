# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 09:28:25 2018

@author: Alexander
"""

import pandas as pd
import os

df = pd.read_pickle( "C://Users//Alexander//Documents//Python//olmedo-vinueza-alexander-daniel//03-Spyder//data//artwork_data_frame.pickle")

df.loc[1035,'artist']

df.iloc[0,1]

df.iloc[0,:]

df.iloc[0:2,0:2]

df['heigth']*df['width']

