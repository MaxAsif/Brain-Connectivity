# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:09:14 2019

@author: Asif
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# READ FORAMTTED DATA
df = pd.read_csv("out.csv")

# PLOT TIME-SERIES DATA
df[['FP1','FP2']].plot()
plt.show()

# IMPORT GCM MODEL
from statsmodels.tsa.stattools import grangercausalitytests

# ALL CHANNELS LIST
channels = df.columns.tolist()
channels = channels[1:]

# CREATE 2D MATRIX
data = {}
for chn in channels:
    values = []
    for chn1 in channels:
        val = grangercausalitytests(df[[chn,chn1]],maxlag = 2)[2][0]['params_ftest'][1]
        values.append(val)
    data[chn] = values
    
df1 = pd.DataFrame(data)

# EXPORT FILE
df1.to_csv('2d-Graph.csv', encoding='utf-8', index=False)

# PLOT THE 2D GRAPH 
H = df1.to_numpy()  # added some commas and array creation code

fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(H)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()