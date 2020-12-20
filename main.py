from graphics import *
import utils
from Graph import Graph
import time
from configs import get_configs
g = {
    'a': {'b', 'c', 'd'},
    'b': {'a', 'e'},
    'c': {'a', 'e', 'd', 'f'},
    'd': {'a', 'c', 'h'},
    'e': {'b', 'c', 'g'},
    'f': {'c', 'g', 'h'},
    'g': {'e', 'f'},
    'h': {'f', 'd'}
}

depths = [
    ['a'],
    ['b', 'c', 'd'],
    ['e', 'f'],
    ['g', 'h']
]

configs = get_configs()

def plot_graph_2():
    win = GraphWin('Graph Plot', configs.win_width, configs.win_height)
    win.setBackground('white')

    edges = [{'a', 'b'}, {'a', 'c'}, {'a', 'd'}, {'b', 'e'}, {'c', 'e'}, {'c', 'd'}, {'c', 'f'}, {'d', 'h'}, {'e', 'g'}, {'f', 'g'}, {'f', 'h'}]

    adj_list = utils.to_adj_list(edges)
    print(adj_list)
    g = Graph(adj_list).default()

    # Draw points
    for node in g['nodes']:
        m = Text(node.point, node.name)
        m.setSize(20)
        m.setTextColor('red')
        m.draw(win)

    # Draw lines
    for edge in g['edges']:
        print (edge)
        print (edge[0].point, edge[1].point)
        l = Line(edge[0].point, edge[1].point)
        l.draw(win)
        
    win.getMouse()
    win.close()
    

plot_graph_2()
