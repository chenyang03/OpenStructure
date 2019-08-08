# Please use conda to install the following libraries
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

# We add the following new funcntions based on the networkx library

# Hierarchy is a form of closure in which a minority of contacts, typically one or two, stand above the others for being more the source of closure.
def hierarchy(G, nodes=None, weight=None):
    '''Returns the hierarchy of all nodes in the graph G'''
    if nodes is None:
         nodes = G
    hierarchy = {}
    for v in nodes:
        if len (G[v])== 0:
            hierarchy[v] == float('nan')
            continue
        N = len (G[v])
        constraint_v = nx.constraint(G,[v])
        temp = 0
        for j in G[v]:
            temp = temp+(nx.local_constraint(G, v, j)/(constraint_v[v]/N))*np.log(nx.local_constraint(G, v, j)/(constraint_v[v]/N))
        hierarchy[v] = temp/(N*np.log(N))
    return hierarchy

