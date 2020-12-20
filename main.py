from graphics import *
import utils
from Graph import Graph
import time

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

WIN_HEIGHT = 600
WIN_WIDTH = 600

def plot_graph():
    win = GraphWin('Graph Plot', WIN_HEIGHT, WIN_WIDTH)
    win.setBackground('white')

    num_layers = len(depths)
    max_width = 0
    for node_list in depths:
        if len(node_list) > max_width:
            max_width = len(node_list)

    layer_height = WIN_HEIGHT//(num_layers - 1)

    
    # Draw points
    node_points = dict()
    for depth, node_list in enumerate(depths):
        num_nodes = len(node_list)
        spacing = WIN_WIDTH//(num_nodes + 1)

        for i, node in enumerate(node_list):
            x_pos = depth * layer_height
            y_pos = spacing * (i + 1)
            node_points[node] = Point(x_pos, y_pos)
            print ("Drawing {} at ({}, {})".format(node, x_pos, y_pos))
            message = Text(Point(x_pos, y_pos), node)
            message.setSize(20)
            message.setTextColor('red')
            message.draw(win)

    # Draw lines:
    for node1 in node_points:
        p1 = node_points[node1]
        for node2 in g[node1]:
            p2 = node_points[node2]
            l = Line(p1, p2)
            l.draw(win)
            
    win.getMouse()
    win.close()
# plot_graph()






def plot_graph_2():
    win = GraphWin('Graph Plot', 1300, 1300)
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
