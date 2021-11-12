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

	for k in range(2*len(nodes_names)):
		
		alphabet_temp = nodes_names
		first_random = random.choice(alphabet_temp)
		alphabet_temp = alphabet_temp.replace(first_random,"")
		second_random = random.choice(alphabet_temp)
		G.add_edge(first_random, second_random)
	
	nx.draw(G, with_labels=True)
	time.sleep(2)

ani = animation.FuncAnimation(fig, animate, frames=6, interval=1000, repeat=True)

plt.show()
