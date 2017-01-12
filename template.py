from edgy import *

def stepFig(G, position):
    yield

if __name__ == '__main__':
    G = nx.Graph()
    position = nx.spring_layout(G)
    for step in stepFig(G, position):
        show(G, setPos=position)
        pylab.pause(0.001)
        pylab.cla()


