from Node import Node
from copy import deepcopy
from GraphAlgorithm import GraphAlgorithm
import logging
from configs import get_configs


class Graph:

    def __init__(
            self,
            adj_list: dict=None
    ) -> None:
        '''
        adj_list: dict with keys as Node types and values as set of Nodes types
        '''
        self.adj_list = adj_list

        self.reprs = {
            'default': None,
            'bipartite': None,
            'bfs': None,
            'dfs': None,
            'bfs_tree': None,
            'dfs_tree': None
        }

        self.configs = get_configs()

    def default(self):
        if self.reprs['default']:
            return self.reprs['default']
        else:
            self.reprs['default'] = self._get_default_repr()
            return self.reprs['default']
        
    def bipartite(self):
        pass

    def bfs(self, start: Node, end:Node)->None:
        pass

    def dfs(self, start:Node, end:Node)->None:
        pass

    def bfs_tree(self, start:Node, end:Node)->None:
        pass

    def dfs_tree(self, start:Node, end:Node)->None:
        pass
                
    
    ############## private methods ###############

    def _get_default_repr(self):
        '''
        simple bfs based
        '''
        default_repr = {
            'nodes': set(),
            'edges': set()
        }
        
        adj_list = deepcopy(self.adj_list)
        depths, _ = GraphAlgorithm(adj_list).bfs(list(adj_list.keys())[0])
        
        num_layers = len(depths)

        max_width = 0
        for node_list in depths:
            if len(node_list) > max_width:
                max_width = len(node_list)

        layer_height = self.configs.win_height//(num_layers - 1)
    
        # set points
        node_points = dict()
        for depth, node_list in enumerate(depths):
            num_nodes = len(node_list)
            spacing = self.configs.win_width//(num_nodes + 1)
            
            for i, node in enumerate(node_list):
                x_pos = depth * layer_height
                y_pos = spacing * (i + 1)
                node.set_pos(x_pos, y_pos)
                default_repr['nodes'].add(node)
                node_points[node] = node
        
        # set edges:
        seen = set()
        for node1 in adj_list:
            for node2 in adj_list[node1]:
                node1 = node_points[node1]
                node2 = node_points[node2]

                if not (node1, node2) in seen and not (node2, node1) in seen:
                    default_repr['edges'].add((node1, node2))
                    seen.add((node1, node2))
                

        return default_repr
