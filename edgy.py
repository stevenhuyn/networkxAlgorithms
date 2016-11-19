import networkx as nx
import pylab
from collections import deque

try:
    from Queue import PriorityQueue
except ImportError:
    from queue import PriorityQueue

# Turns on interactive mode for the matplotlib graphs
# and allows for animations
# No clue what this actually does
pylab.ion()

def show(G, node_attribute = "id", edge_attribute = "label", node_size=1250,
         setPos=None, labelPos=0.5):

    if setPos == None:
        # If position doesn't matter generate spring layout
        layout = nx.spring_layout(G)
    else:
        # If position already set aka for animation
        layout = setPos

    for v, data in G.nodes(data = True):
        if "x" in data:
            layout[v] = [data["x"], layout[v][1]]
        if "y" in data:
            layout[v] = [layout[v][0], data["y"]]

    node_colors = [G.node[v].get("color", "white") for v in G.nodes()]
    edge_colors = [G.edge[e[0]][e[1]].get("color", "black") for e in G.edges()]
    edge_width = [G.edge[e[0]][e[1]].get("width", 1) for e in G.edges()]
    
    node_labels = dict((v, v if node_attribute == "id" else G.node[v].get(node_attribute, v))
        for v in G.nodes())
    edge_labels = dict((e, G.edge[e[0]][e[1]].get(edge_attribute, "")) for e in G.edges())    
    
    nx.draw(G, layout, node_color = node_colors, node_size=node_size,
            edge_color = edge_colors, width=edge_width)    
    nx.draw_networkx_labels(G, layout, node_labels)
    nx.draw_networkx_edge_labels(G, layout, edge_labels, label_pos=labelPos)
    
