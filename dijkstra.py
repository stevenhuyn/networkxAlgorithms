from edgy import *
import random
from itertools import combinations

def generate(n):
    G = nx.grid_graph([n, n])

    for first, second, data in G.edges(data=True):
        data['weight'] = random.randint(1, 10)

    return G

def dij(G, pos):
    # Used for the min function later
    lamKeyFunc = lambda n: G.node[n]['tentative']

    # Main loop
    for startNode, destNode in combinations(G.nodes(), 2):
        nx.set_node_attributes(G, 'tentative', float('inf'))
        nx.set_node_attributes(G, 'predecessor', None)
        nx.set_node_attributes(G, 'color', 'white')
        nx.set_edge_attributes(G, 'color', 'black')
        nx.set_edge_attributes(G, 'width', 1)
        G.node[startNode]['color'] = 'blue'
        G.node[destNode]['color'] = 'blue'
        G.node[startNode]['tentative'] = 0
        unvisited = sorted(list(G.nodes()), key=lamKeyFunc)
        
        u = unvisited[0]
        unvisited.pop(0)

        """
        Below is the main loop to calculate the tentative of nodes
        The amount depends on the loop conditional below
        
        Top is assuming graph is connected so that all nodes are reachable
        This is so the the spanning tree is completed (red edges)

        Bottom is to just use the algo to find shortest path and also
        assumes that the destination node is reachable.
        """
##        while unvisited != []:
        while u != destNode:    
            for v in G.neighbors(u):
                alt = G.node[u]['tentative'] + G.edge[u][v]['weight']
                G.edge[u][v]['color'] = 'red'
                yield True
                G.edge[u][v]['color'] = 'black'
                
                if alt < G.node[v]['tentative']:
                    G.node[v]['tentative'] = alt
                    G.node[v]['predecessor'] = u

            if u not in [startNode, destNode]:
                G.node[u]['color'] = 'red'
                
            yield True

            unvisited.sort(key=lamKeyFunc)
            u = unvisited[0]
            unvisited.pop(0)

        # Reset tree for the solution
        nx.set_node_attributes(G, 'color', 'white')
        nx.set_edge_attributes(G, 'color', 'black')
        nx.set_edge_attributes(G, 'width', 1)
        G.node[startNode]['color'] = 'blue'
        G.node[destNode]['color'] = 'blue'
        
        # Create spanning tree
        for node in G.nodes():
            prev = G.node[node]['predecessor']
            if prev == None:
                continue
            else:
                G.edge[node][prev]['color'] = 'red'
                G.edge[node][prev]['width'] = 3
                
            yield True

        # Create Path
        second, first = destNode, G.node[destNode]['predecessor']
        while True:
            G.edge[first][second]['color'] = 'green'
            G.edge[first][second]['width'] = 5
            first = second
            second = G.node[first]['predecessor']
            
            yield True
            
            if second == None:
                break
            elif second != startNode:
                G.node[second]['color'] = 'green'

        yield False

    yield None

def showAllSteps(G, position):
    for step in dij(G, position):
        show(G, setPos=position, edge_attribute='weight', labelPos=0.4)
        pylab.pause(0.00001)
        if step:   
            pylab.cla()
        elif not step:
            pylab.pause(0)
            pylab.cla()
        else:
            break

def showPathOnly(G, position):
    for step in dij(G, position):
        if step:   
            continue
        else:
            pylab.pause(0.1)
            pylab.cla()
        show(G, setPos=position, edge_attribute='weight', labelPos=0.4)

if __name__ == '__main__':
    while True:
        G = generate(4)
        position = nx.spring_layout(G)
##        showPathOnly(G, position)
        showAllSteps(G, position)

