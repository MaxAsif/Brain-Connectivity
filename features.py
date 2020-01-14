# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:41:06 2019

@author: Asif
"""
from numpy import genfromtxt
import numpy as np
import networkx as nx
import pandas as pd

mydata = genfromtxt('2d-Graph.csv', delimiter=',')
# print(mydata)
# print(type(mydata))
adjacency = mydata[1:,:]
# print(adjacency)

# adjacency = mydata[1:7,:6]
G = nx.DiGraph(adjacency)
# nx.draw(G)
nx.clustering(G,weight="weight")
nx.average_clustering(G,weight="weight")

r=nx.degree_assortativity_coefficient(G,weight="weight")
print("%3.1f"%r)