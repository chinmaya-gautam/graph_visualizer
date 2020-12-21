from collections import deque
from Node import Node

class GraphAlgorithm:

    def __init__(self, adj_list: dict) -> None:
        self.adj_list = adj_list


    def bfs(self, root: Node) -> list:
        return self._bfs_iterative(root)

    def _bfs_iterative(self, root: Node) -> list:

        queue = deque()
        depths = list()
        visited = set()
        edges = list()
        
        visited.add(root)
        queue.append((root, 1))

        while queue:
            current, node_depth = queue.popleft()
            if current in self.adj_list:
                for child in self.adj_list[current]:
                    if child not in visited:
                        queue.append((child, node_depth + 1))
                        edges.append((current, child))
                        visited.add(child)
            if node_depth > len(depths):
                depths.append([current])
            else:
                depths[node_depth - 1].append(current)
        return depths, edges

    def dfs(self, root: Node) -> list:
        return self._dfs_iterative(root)

    def _dfs_iterative(self, root: Node) -> list:

        stack = list()
        depths = list()
        visited = set()
        edges = list()
        
        stack.append((root, 1, None))
        
        while stack:
            current, node_depth, parent = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            if parent:
                edges.append((parent, current))
            if current in self.adj_list:
                for child in self.adj_list[current]:
                    if child not in visited:
                        stack.append((child, node_depth + 1, current))

            if node_depth > len(depths):
                depths.append([current])
            else:
                depths[node_depth - 1].append(current)

        return depths, edges


if __name__ == "__main__":
    adj_list = {
        Node('a'): {Node('b'), Node('c'), Node('d')},
        Node('b'): {Node('a'), Node('e')},
        Node('c'): {Node('a'), Node('e'), Node('d'), Node('f')},
        Node('d'): {Node('a'), Node('c'), Node('h')},
        Node('e'): {Node('b'), Node('c'), Node('g')},
        Node('f'): {Node('c'), Node('g'), Node('h')},
        Node('g'): {Node('e'), Node('f')},
        Node('h'): {Node('f'), Node('d')}
    }

    depths, edges = GraphAlgorithm(adj_list).bfs(Node('a'))

    for row in depths:
        print(row)
        

    print (edges)
