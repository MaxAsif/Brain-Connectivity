# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
# READING CSV FILES
df = pd.read_csv("co2a0000364.csv")

# REMOVING UNNECESSARY COLUMNS
df = df[df.columns[1:4]]

# REMOVE HEADERFILES
df = df.drop(df.index[0])
df = df.drop(df.index[0])
df = df.drop(df.index[0])

# RENAME COLUMNS
df = df.rename(columns={"co2a0000364.rd":"chan", "Unnamed: 2":"Time", "Unnamed: 3":"Voltage"})

# REEMOVE ROWS IN BETWEEN
df = df[df.Time != 'chan']

# RESET INDEX 
df = df.reset_index()
df = df[df.columns[1:4]]

df.count()
# ALL CHANNELS NAME LIST
channels = df.chan.unique().tolist()

# LOOP TO ORIENT DATA
i = 0
for chn in channels:
    df1 = df.loc[[*range(i,i+256,1)],['Voltage']].reset_index()
    df1 = df1[df1.columns[1:]]
    df[chn] = df1
    i = i+256

# DROPS ROWS after    
df = df.drop(df.index[256:])

df = df.drop(["chan","Voltage"],axis = 1)

# EXPORT TO CSV FILES
df.to_csv('out.csv', encoding='utf-8', index=False)