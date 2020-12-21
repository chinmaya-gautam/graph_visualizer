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
        self.configs = get_configs()

        self.reprs = {
            'bipartite': dict(),
            'bfs': dict(),
            'dfs': dict(),
            'bfs_tree': dict(),
            'dfs_tree': dict()
        }
    def default(self, root: Node=None):
        return self.bfs(root)
        
    def bipartite(self):
        pass

    def bfs(self, root: Node, end:Node=None)->None:
        if root:
            root = Node(root)

        if root not in self.reprs['bfs']:
            self.reprs['bfs'][root] = self._get_bfs_repr(root)
        return self.reprs['bfs'][root]

    def dfs(self, root:Node, end:Node=None)->None:
        if root:
            root = Node(root)

        if root not in self.reprs['dfs']:
            self.reprs['dfs'][root] = self._get_dfs_repr(root)
        return self.reprs['dfs'][root]


    def bfs_tree(self, root:Node, end:Node=None)->None:
        if root:
            root = Node(root)

        if root not in self.reprs['bfs_tree']:
            self.reprs['bfs_tree'][root] = self._get_bfs_tree_repr(root)
        return self.reprs['bfs_tree'][root]


    def dfs_tree(self, root:Node, end:Node=None)->None:
        if root:
            root = Node(root)

        if root not in self.reprs['dfs_tree']:
            self.reprs['dfs_tree'][root] = self._get_dfs_tree_repr(root)
        return self.reprs['dfs_tree'][root]

                
    
    ############## private methods ###############

    def _get_bfs_repr(self, root):
        '''
        simple bfs based
        '''
        bfs_repr = {
            'nodes': set(),
            'edges': set()
        }
        
        adj_list = deepcopy(self.adj_list)

        if not root:
            root = list(adj_list.keys())[0]

        depths, _ = GraphAlgorithm(adj_list).bfs(root)
        
        num_layers = len(depths)

        max_width = 0
        for node_list in depths:
            if len(node_list) > max_width:
                max_width = len(node_list)

        layer_height = (self.configs.win_height - self.configs.y_padding * 2)//(num_layers - 1)
    
        # set points
        node_points = dict()
        for depth, node_list in enumerate(depths):
            num_nodes = len(node_list)
            spacing = (self.configs.win_width - self.configs.x_padding * 2)//(num_nodes + 1)
            
            for i, node in enumerate(node_list):
                x_pos = depth * layer_height + self.configs.x_padding
                y_pos = spacing * (i + 1) + self.configs.y_padding
                node.set_pos(x_pos, y_pos)
                bfs_repr['nodes'].add(node)
                node_points[node] = node
        
        # set edges:
        seen = set()
        for node1 in adj_list:
            for node2 in adj_list[node1]:
                node1 = node_points[node1]
                node2 = node_points[node2]

                if not (node1, node2) in seen and not (node2, node1) in seen:
                    bfs_repr['edges'].add((node1, node2))
                    seen.add((node1, node2))
                

        return bfs_repr
    
    def _get_bfs_tree_repr(self, root):
        '''
        simple bfs based
        '''
        bfs_tree_repr = {
            'nodes': set(),
            'edges': set()
        }
        
        adj_list = deepcopy(self.adj_list)

        if not root:
            root = list(adj_list.keys())[0]

        depths, edges = GraphAlgorithm(adj_list).bfs(root)
        
        num_layers = len(depths)

        max_width = 0
        for node_list in depths:
            if len(node_list) > max_width:
                max_width = len(node_list)

        layer_height = (self.configs.win_height - self.configs.y_padding * 2)//(num_layers - 1)
    
        # set points
        node_points = dict()
        for depth, node_list in enumerate(depths):
            num_nodes = len(node_list)
            spacing = (self.configs.win_width - self.configs.x_padding * 2)//(num_nodes + 1)
            
            for i, node in enumerate(node_list):
                x_pos = depth * layer_height + self.configs.x_padding
                y_pos = spacing * (i + 1) + self.configs.y_padding
                node.set_pos(x_pos, y_pos)
                bfs_tree_repr['nodes'].add(node)
                node_points[node] = node
        
        # set edges:
        for edge in edges:
            bfs_tree_repr['edges'].add(edge)

        return bfs_tree_repr

    def _get_dfs_repr(self, root):
        '''
        simple dfs based
        '''
        dfs_repr = {
            'nodes': set(),
            'edges': set()
        }
        
        adj_list = deepcopy(self.adj_list)

        if not root:
            root = list(adj_list.keys())[0]

        depths, _ = GraphAlgorithm(adj_list).dfs(root)
        
        num_layers = len(depths)

        max_width = 0
        for node_list in depths:
            if len(node_list) > max_width:
                max_width = len(node_list)

        layer_height = (self.configs.win_height - self.configs.y_padding * 2)//(num_layers - 1)
    
        # set points
        node_points = dict()
        for depth, node_list in enumerate(depths):
            num_nodes = len(node_list)
            spacing = (self.configs.win_width - self.configs.x_padding * 2)//(num_nodes + 1)
            
            for i, node in enumerate(node_list):
                x_pos = depth * layer_height + self.configs.x_padding
                y_pos = spacing * (i + 1) + self.configs.y_padding
                node.set_pos(x_pos, y_pos)
                dfs_repr['nodes'].add(node)
                node_points[node] = node
        
        # set edges:
        seen = set()
        for node1 in adj_list:
            for node2 in adj_list[node1]:
                node1 = node_points[node1]
                node2 = node_points[node2]

                if not (node1, node2) in seen and not (node2, node1) in seen:
                    dfs_repr['edges'].add((node1, node2))
                    seen.add((node1, node2))
                

        return dfs_repr

    def _get_dfs_tree_repr(self, root):
        '''
        simple dfs based
        '''
        dfs_tree_repr = {
            'nodes': set(),
            'edges': set()
        }
        
        adj_list = deepcopy(self.adj_list)

        if not root:
            root = list(adj_list.keys())[0]

        depths, edges = GraphAlgorithm(adj_list).dfs(root)
        
        num_layers = len(depths)

        max_width = 0
        for node_list in depths:
            if len(node_list) > max_width:
                max_width = len(node_list)

        layer_height = (self.configs.win_height - self.configs.y_padding * 2)//(num_layers - 1)
    
        # set points
        node_points = dict()
        for depth, node_list in enumerate(depths):
            num_nodes = len(node_list)
            spacing = (self.configs.win_width - self.configs.x_padding * 2)//(num_nodes + 1)
            
            for i, node in enumerate(node_list):
                x_pos = depth * layer_height + self.configs.x_padding
                y_pos = spacing * (i + 1) + self.configs.y_padding
                node.set_pos(x_pos, y_pos)
                dfs_tree_repr['nodes'].add(node)
                node_points[node] = node
        
        # set edges:
        for edge in edges:
            dfs_tree_repr['edges'].add(edge)

        return dfs_tree_repr
