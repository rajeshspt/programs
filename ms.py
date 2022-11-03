# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 00:08:55 2022

@author: SPTINT-23
"""

import pandas as pd
 

import numpy as np

dict = {'First_Score':[100, 90, np.nan, 95],
        'Second_Score': [30, 45, 56, np.nan],
        'Third':[np.nan, 40, 80, 98]}

df = pd.DataFrame(dict)
print(df)
 

print(df.isnull())
print(df.notnull())
print(df.fillna(0))
a=df.fillna(method='pad')
print(a)
b=df.fillna(method='bfill')
print(b)
print(df.dropna())
c=df["Third"].fillna("other")
print(c)



 