# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:48:06 2022

@author: SPTINT-23
"""

import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/SPTINT-23/Desktop/dataset/spt.csv")
print(a)
b=a.groupby('dept')
print(a.sum())
print(a.agg({'salary':['min','max','sum']}))
pivot=a.pivot_table(index=['year'],values=['id'])
print(pivot)