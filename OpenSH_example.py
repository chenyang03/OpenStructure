from OpenSH_lib import *

# sample topologies are from Figure 2 of the paper
#
# Ronald S. Burt, Martin Kilduff, and Stefano Tasselli. Social Network Analysis: Foundations and Frontiers on Advantage. Annual Review of Psychology, 2013, 64:527-547.
#
#

network_size_list = [3, 5, 10]

for network_size in network_size_list:
    G = nx.Graph()
    # add the nodes to the graph
    for i in range(0, network_size+1):
        G.add_node(i)
    # add the edges to the graph
    for i in range(1, network_size+1):
        G.add_edge(0, i)
    for i in range(2, network_size+1):
        G.add_edge(1, i)
    #print(G.number_of_nodes(), G.number_of_edges())
    print('========')
    print('Size of the Ego:', network_size)
    print('Constraint:', nx.constraint(G, [0]))
    print('Hierarchy:', hierarchy(G, [0]))


