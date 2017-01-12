from edgy import *
import copy

"""
Might try next time to merge label dictionaries and use \n instead
"""

def generate():
    G = nx.DiGraph()
    G.add_edges_from([('A', 'B')], weight=8)
    G.add_edges_from([('A', 'C')], weight=-2)
    G.add_edges_from([('A', 'D')], weight=4)
    G.add_edges_from([('C', 'B')], weight=7)
    G.add_edges_from([('C', 'D')], weight=1)
    G.add_edges_from([('B', 'E')], weight=-2)
    G.add_edges_from([('C', 'E')], weight=3)
    G.add_edges_from([('F', 'C')], weight=9)
    G.add_edges_from([('D', 'F')], weight=5)
    return G
    

def stepFig(G, pos, init='A'):
    # Intiate node sand shit
    for node in G.nodes():
        G.node[node]['tentative'] = floa
        t('inf')
    G.node[init]['tentative'] = 0
    
    for i in range(len(G.nodes()) - 1):
        change = False
        for e in G.edges():
            u, v = e
            current = G.node[v]['tentative']
            candidate = G.node[u]['tentative'] + G.edge[u][v]['weight']
            if candidate < current:
                change = True
                G.node[v]['tentative'] = candidate
            else:
                G.node[v]['tentative'] = current
            yield True
            
        if change == False:
            break
        
    yield False

def dicMerge(a, b):
    # https://stackoverflow.com/questions/17604837/python-combine-two-dictionaries-concatenate-string-values
    """
    Fuck this shit's noice yo
    """
    keys = a.keys() | b.keys()  # wtf is this bullshit
    return {k : str(a.get(k, '')) + ' ' + str(b.get(k, '')) for k in keys}

if __name__ == '__main__':
    G = generate()
    position = nx.shell_layout(G)
    lblNode = {i: i for i in G.nodes()}
    
    
##    posNode = copy.deepcopy(position)
##    posTent = copy.deepcopy(position) 
##    for p in list(position.keys()):
##        # Arrays seem to be referenced
##        posNode[p][1] += 0.05
##        posTent[p][1] -= 0.05

    for step in stepFig(G, position):
        lblTent = nx.get_node_attributes(G, 'tentative')
        lblBoth = dicMerge(lblNode, lblTent)
        nx.draw_networkx_labels(G, position, labels=lblBoth, font_size=13)
        show(G, setPos=position, node_attribute=None, edge_attribute='weight', labelPos=0.4)
        pylab.pause(0.001)
        if step:
            pylab.clf()


