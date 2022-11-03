# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:02:19 2022

@author: SPTINT-23
"""

import pandas as pd 
import numpy as np
  
 
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([3, 4, 5, 6, 7])
union = pd.Series(np.union1d(ser1, ser2))  
intersect = pd.Series(np.intersect1d(ser1,ser2))
notcommonseries = union[union.isin(intersect)]
print(notcommonseries)