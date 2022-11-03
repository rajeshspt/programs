# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 02:34:57 2022

@author: SPTINT-23
"""

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-23/Desktop/dataset/tips.csv")
print(data.head(10))
plt.hist(data['tip'])
plt.title("histogram")
plt.legend()
plt.show()