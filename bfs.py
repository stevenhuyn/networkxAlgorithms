from edgy import *

def bfs(G, pos):
    """
    Breadth first search

    Input params
    G:      Nx Graph
    pos:    Set positions of the nodes

    Graph legend
    red:    Currently searching
    blue:   Already searched
    green:  Neighbour, not searched yet
    """
    visited = deque()
    for startNode in G.nodes():
        nx.set_node_attributes(G, 'color', 'white')
        visited.appendleft(startNode)
        yield True
        
        while visited != deque():
            look = visited[0]
            visited.popleft()
            G.node[look]['color'] = 'red'
            yield True
            
            newNeigh = [ neigh for neigh in G.neighbors(look)
                         if G.node[neigh]['color'] not in
                         ['green', 'blue', 'red'] ]
            for neigh in newNeigh:
                G.node[neigh]['color'] = 'green'
                yield True
                
            visited.extend(newNeigh) # Important
            G.node[look]['color'] = 'blue'
            
        yield False
        
if __name__ == '__main__':
    while True:
        G = nx.grid_graph([4, 4])
        position = nx.spring_layout(G)
        for step in bfs(G, position):
            show(G, setPos=position)
            if step == True:
                pylab.pause(0.0001)
            else: # step == False
                pylab.pause(1)
            pylab.clf()
        
