from heapq import heappop, heappush

class Edge:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.head.out_edges.append(self)
        self.tail.in_edges.append(self)
        self.price = 0
        self.time = 0
        self.distance = 0

class Node:
    def __init__(self, name):
        self.name = name
        self.out_edges = []

def short_path(start_node, end_node, weight_func=lambda edge: 1):

    shortest_paths = {start_node: (0, None)}

    edge_heap = []
    for edge in start_node.out_edges:
        heappush(edge_heap, (weight_func(edge), edge))

    while edge_heap:
        path_weight, edge = heappop(edge_heap)
        if ((edge.head not in shortest_paths) or
            (shortest_paths[edge.head][0] > path_weight)):
            shortest_paths[edge.head] = (path_weight, edge)
            for out_edge in edge.head.out_edges:
                heappush(edge_heap, (path_weight + weight_func(out_edge),
                                        out_edge))
    if end_node not in shortest_paths:
        err = ("No connection from node %s" % str(start_node) +
                " to node %s." % str(end_node))
        raise NoPathGraphException(err)
    path_weight = shortest_paths[end_node][0]
    path_edges = [shortest_paths[end_node][1]]
    current_node = path_edges[-1].tail
    while current_node is not start_node:
        path_edges.append(shortest_paths[current_node][1])
        current_node = path_edges[-1].tail
    return path_edges[::-1], path_weight

class NoPathGraphException(Exception):
    pass

short_path(Node("A"), Node("B"), lambda edge: edge.distance)