from matplotlib import pyplot as plt, animation
import numpy as np
import networkx as nx
import random
import time 

##Display Configuration##

plt.rcParams["figure.figsize"] = [16, 7.50]
plt.rcParams["figure.autolayout"] = True

##Global Variables Initialization##

global weight_edge
global edges

##Create Graph with its nodes##

fig = plt.figure()
G = nx.Graph()
nodes_names = "ABCD"
G.add_nodes_from(list(nodes_names))	

##Create random edges##

for k in range(2*len(nodes_names)):

	alphabet_temp = nodes_names
	first_random = random.choice(alphabet_temp)
	alphabet_temp = alphabet_temp.replace(first_random,"")
	second_random = random.choice(alphabet_temp)
	if ([first_random, second_random] not in list(G.edges)):
		G.add_edge(first_random, second_random, weight = 0)

##Display Graph without edges labels##

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos)

##Create lists of edges and their weight##

edges = list(G.edges)
weight_edge = np.zeros(len(edges), dtype = int)

def update(frame):

	global weight_edge
	global edges

	##Clear edges labels##
	
	G.remove_edges_from(edges)
	
	##Recreate edges with their new weight##

	for k in range(len(edges)):
		G.add_edge(edges[k][0], edges[k][1], weight = weight_edge[k])
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

	##Increase or Decrease randomly an edge weight##

	chosen = random.randint(0, len(weight_edge) - 1)
	weight_edge[chosen] = random.choice([weight_edge[chosen] - 1, weight_edge[chosen] + 1])

	#time.sleep(1)

##Trigger the animation##

anim = animation.FuncAnimation(fig, update, frames=10, interval=1000, repeat=True)
plt.show()
