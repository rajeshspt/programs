# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 22:57:34 2022

@author: SPTINT-23
"""
import pandas as pd
df = pd.DataFrame({'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']})

print(df[['Name', 'Address']])
