from Node import Node

def to_adj_list(edges):

    adj_list = dict()

    for edge in edges:
        node1, node2 = map(lambda x: Node(x), edge)
        
        if node1 not in adj_list:
            adj_list[node1] = {node2, }
        else:
            adj_list[node1].add(node2)

        if isinstance(edge, set):
            if node2 not in adj_list:
                adj_list[node2] = {node1, }
            else:
                adj_list[node2].add(node1)

    return adj_list
