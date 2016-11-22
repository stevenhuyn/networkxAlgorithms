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
        yield True
        visited.appendleft(startNode)
        while visited != deque():
            look = visited[0]
            visited.popleft()
            G.node[look]['color'] = 'red'
            yield True
            newNeigh = [ neigh for neigh in G.neighbors(look)
                                 if G.node[neigh]['color'] != 'green' and G.node[neigh]['color'] != 'red']
            for neigh in newNeigh:
                G.node[neigh]['color'] = 'green'
            visited.extend(newNeigh) # Important
            yield True
            G.node[look]['color'] = 'green'
            

if __name__ == '__main__':
    for file in [f for f in glob.glob(".\dot\*.txt")]:
        G = generate(6)
        position = nx.spring_layout(G)
        for step in bfs(G, position):
            show(G, setPos=position)
            pylab.pause(0.001)
            pylab.clf()
        
