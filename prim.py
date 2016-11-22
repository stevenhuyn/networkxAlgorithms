from edgy import *
import random

def generate(n):
    """
    Generate a complete graph with n nodes
    """

    G = nx.gnp_random_graph(n, random.randint(1, 100))

    for first, second, data in G.edges(data=True):
        data['weight'] = random.randint(1, 10)

    return G

def prim(G, pos):
    """
    Visually runs Prim's algorithm on G with given position
    to maintain position for the animation
    """
    # Setup
    connected = set()
    connected.add(list(G.nodes())[0])

    # Initialise edges to grey
    nx.set_edge_attributes(G, 'color', 'grey')
    
    yield
    
    # Main loop
    while nx.number_of_nodes(G) != len(connected):
        # Generate list of potentials
        potential = set()
        for node in connected:
            for neighbour in G.neighbors(node):
                if neighbour not in connected:
                    weight = G.get_edge_data(node, neighbour)['weight']
                    potential.add((weight, node, neighbour))

        #  Calculate least edge and set colour
        leastEdge = min(potential)
        weight, node, neighbour = leastEdge
        connected.add(neighbour)
        G.edge[node][neighbour]['color'] = 'red'
        G.edge[node][neighbour]['width'] = 3

        yield True
    
    yield False

if __name__ == '__main__':
    while True:
        G = generate(10)
        position = nx.shell_layout(G)
        for keepGoing in prim(G, position):
            show(G, edge_attribute='weight', setPos=position, labelPos=0.4)
            # Matplotlib implmentation of pausing graph
            pylab.pause(0.001)
            pylab.clf()
