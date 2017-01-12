from edgy import *

def generate_graph():
    G = nx.Graph()

    G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])
    G.add_edges_from([('A', 'B'),
                      ('A', 'C'),
                      ('A', 'D'),
                      ('B', 'C'),
                      ('B', 'E'),
                      ('C', 'E'),
                      ('C', 'F'),
                      ('C', 'D'),
                      ('D', 'F')])
    return G

def stepFig(G, position):
    lenEdge = len(G.edges())
    pylab.title('# of edges: ' + str(lenEdge))
    yield True
    for mid in G.nodes():
        for start in G.nodes():
            for end in G.nodes():
                if start == end or end == mid:
                    # Not in the pseudocode
                    continue
                if not G.has_edge(start, end):
                    # If not existing transitive closure
                    if G.has_edge(start, mid) and G.has_edge(mid, end):
                        G.add_edge(start, end)
                        lenEdge += 1
                        G.edge[start][end]['color'] = 'red'
                        pylab.title('# of edges: ' + str(lenEdge))
                        yield True
                        G.edge[start][end]['color'] = 'black'
    pylab.title('Completed\n# of edges: ' + str(lenEdge))
    yield False
        

if __name__ == '__main__':
    G = generate_graph()
    position = nx.spring_layout(G)
    for step in stepFig(G, position):
        show(G, setPos=position)
        pylab.pause(1)
        if step:
            pylab.cla()


