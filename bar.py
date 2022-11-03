# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 02:28:12 2022

@author: SPTINT-23
"""
#bar  plot
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/SPTINT-23/Desktop/dataset/tips.csv")
print(data.head(10))
plt.bar(data['day'],data['tip'])
plt.title("bar plot")
plt.xlabel('day')
plt.ylabel('tip')
plt.legend()
plt.show()