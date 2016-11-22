from edgy import *
import glob
import random

def generate(n):
    G = nx.ladder_graph(n)

    for first, second, data in G.edges(data=True):
        data['weight'] = random.randint(1, 10)

    return G

def bfs(G, pos):
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
                         if G.node[neigh]['color'] != 'green'
                         and G.node[neigh]['color'] != 'red']
            for neigh in newNeigh:
                G.node[neigh]['color'] = 'green'
                yield True
                
            visited.extend(newNeigh) # Important
            G.node[look]['color'] = 'green'
            

if __name__ == '__main__':
    while True:
        G = nx.dorogovtsev_goltsev_mendes_graph(3)
        position = nx.spring_layout(G)
        for step in bfs(G, position):
            show(G, setPos=position)
            pylab.pause(0.1)
            pylab.clf()
        
