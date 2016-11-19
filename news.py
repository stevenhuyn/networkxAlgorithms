from edgy import *
import os

def stepFig(G, pos):
    numNodes = G.number_of_nodes()
    size = 1250
    for nodeStart in G.nodes():

        # Reset
        nx.set_node_attributes(G, 'color', 'white')
        
        G.node[nodeStart]['color'] = 'blue'
        oldEdge = [nodeStart]
        newEdge = []
        colourCount = 1
        
        yield False
        
        # While graph is not all green
        while oldEdge != []:
            # Iterate through every neighbour of outer nodes

            nodeNeighbours = set()
            for nodeEdge in oldEdge:
                nodeNeighbours |= set(G.neighbors(nodeEdge))
                for nodeNeigh in nodeNeighbours:
                    
                    if G.node[nodeNeigh]['color']  not in ['blue', 'green']:
                        G.node[nodeNeigh]['color'] = 'green'
                        newEdge.append(nodeNeigh)
                        colourCount += 1
                        
            oldEdge = newEdge
            newEdge = []
            
            yield True

if __name__ == '__main__':
    pylab.ion()
    files = [f for f in os.listdir('.') if f.endswith('.txt')]
    for file in files:
        # By defualt read_dot gives a multigraph which has weird edge accessing shit
        G = nx.Graph(nx.drawing.nx_pydot.read_dot(file))
        position = nx.spring_layout(G)
        for step in stepFig(G, position):
            show(G, setPos=position, node_size=1250)
            pylab.pause(0.1)
            if step:
                pylab.cla()
            elif not step:
                pylab.pause(0.5)
                pylab.cla()
            else:
                break
