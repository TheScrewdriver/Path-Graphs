from matplotlib import pyplot as plt, animation
import numpy as np
import networkx as nx
import random
import time
import string

##########FUNCTIONS##########

##Build Node list##

def node_list(node_number):
	
	L = []

	alphabet = list(string.ascii_uppercase)
	
	if (node_number <= 1 or node_number - 2 > len(alphabet)):
		return L

	L.append("Start")
	for k in range(node_number - 2):
		L.append(alphabet[k])
	L.append("Target")
	return L

##Colorize active edges##

def color_edges(active):

	nx.draw_networkx_edges(
    G,
    pos,
    edgelist = edges,
    width=7,
    alpha=1,
    edge_color="tab:blue",
	)
	
	nx.draw_networkx_edges(
    G,
    pos,
    edgelist=active,
    width=7,
    alpha=1,
    edge_color="tab:red",
	)

##Create a list of random edge capacity##

def capacity_generator(edge_list, max_capacity):
	
	L = []
	for k in range(len(edge_list)):
		n = random.randint(1, max_capacity)
		L.append(n)
	return L

#def car_number_on_nodes(node, score):
#
#	mapping = 
#	G = nx.relabel_nodes(G, mapping)
	
###END(FUNCTIONS)###

##Display Configuration##

plt.rcParams["figure.figsize"] = [16, 7.50]
plt.rcParams["figure.autolayout"] = True

##Global Variables Initialization##

global weight_edge
global edges
global pos
global nodes_names
global nodes_number

nodes_number = 5  #max = 28

##Create Graph with its nodes##

fig = plt.figure()
G = nx.Graph()
nodes_names = node_list(nodes_number)
G.add_nodes_from(nodes_names)
maximum_edges = int((nodes_number * (nodes_number - 1))/2)

##Create random edges##

for k in range(maximum_edges):

	nodes_temp = nodes_names
	random_edge = random.choices(nodes_temp, k=2)
	
	if ([random_edge[0], random_edge[1]] not in list(G.edges)):
		if ([random_edge[1], random_edge[0]] not in list(G.edges)):
			if (random_edge[0] != random_edge[1]):
				G.add_edge(random_edge[0], random_edge[1], weight = 0)

##Display Graph without edges labels##

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos)
nx.draw_networkx_nodes(G, pos, node_size = 5000, node_color = "tab:green")

##Create lists of edges and their weight##

edges = list(G.edges)
weight_edge = np.zeros(len(edges), dtype = int)
capacity_edge = capacity_generator(edges, 5)

##Update animation##
	
def update(frame):

	global weight_edge
	global edges
	global nodes_names
	global pos
	global nodes_number

	chosen_edge = random.randint(0, len(edges) - 1)
	
	##Clear edges labels##
	
	G.remove_edges_from(edges)
	active = []

	##Recreate edges with their new weight##

	for k in range(len(edges)):
		
		G.add_edge(edges[k][0], edges[k][1], weight = str(weight_edge[k]) + "/" + str(capacity_edge[k]))
		if (k == chosen_edge):
			active.append([edges[k][0],edges[k][1]])

	color_edges(active)
	
	elabels = nx.get_edge_attributes(G, 'weight')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = elabels)
	
	##Refresh node labels##

#	node_score = np.zeros(nodes_number, dtype = int)	
#	nodes_names_new = np.zeros(nodes_number, dtype = str)
#	
#	for k in range(len(nodes_names)):
#		
#		nodes_names_new[k] = nodes_names[k] + "\n"
#		pos[nodes_names_new[k]] = pos.pop(nodes_names[k])
#	
#	print("post-pos :", pos)
#	G.add_nodes_from(nodes_names_new)
#	nx.draw_networkx(G, pos)
#	nx.draw_networkx_nodes(G, pos, node_size = 5000)
	
	##Increase or Decrease randomly an edge weight##

	#weight_edge[chosen_edge][0] += random.randint(-1, 1)
	
	#time.sleep(1)

##Trigger the animation##

anim = animation.FuncAnimation(fig, update, frames=10, interval=1000, repeat=True)

plt.show()
