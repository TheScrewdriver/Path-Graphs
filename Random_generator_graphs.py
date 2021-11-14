from matplotlib import pyplot as plt, animation
import networkx as nx
import random
import time 

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

def animate(frame):

	fig.clear()	
	G = nx.Graph()
	nodes_names = "ABCDEFGHI"
	G.add_nodes_from(list(nodes_names))
	weight_list = [1,2,3,4,5]

	for k in range(2*len(nodes_names)):
	
		alphabet_temp = nodes_names
		first_random = random.choice(alphabet_temp)
		alphabet_temp = alphabet_temp.replace(first_random,"")
		second_random = random.choice(alphabet_temp)
		weight_edge = random.choice(weight_list)
		G.add_edge(first_random, second_random, weight=weight_edge)

	pos=nx.spring_layout(G)
	nx.draw_networkx(G,pos)
	labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
	time.sleep(2)

ani = animation.FuncAnimation(fig, animate, frames=6, interval=1000, repeat=True)

plt.show()
