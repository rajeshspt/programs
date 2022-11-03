# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 02:24:24 2022

@author: SPTINT-23
"""
#line plot
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-23/Desktop/dataset/tips.csv")
print(data.head(10))
plt.plot(data['totalbill'])
plt.plot(data['tip'])
plt.title("line plot")
plt.xlabel('totalbill')
plt.ylabel('tip')
plt.legend()
plt.show()