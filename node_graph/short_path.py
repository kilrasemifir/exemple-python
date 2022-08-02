"""Ce module permet de calculer le plus court chemin entre deux noeuds d'un graph"""
from heapq import heappop, heappush


class NoPathGraphException(Exception):
    pass


class Node:
    """Représente un noeud d'un graph"""

    def __init__(self, name, out_edges=[]):
        self.out_edges = out_edges
        self.name = name

    def __repr__(self):
        return self.name


class Edge:
    """Représente une arête d'un graph entre deux noeuds"""

    def __init__(self, tail, head):
        self.head = head
        self.tail = tail

    def __lt__(self, other):
        return False

    def __repr__(self):
        return f"{self.tail} -> {self.head}"

class Ville(Node):
    """Représente une ville"""

    def __init__(self, name, out_edges=[]):
        super().__init__(name, out_edges)



class Route(Edge):
    """Représente une route entre deux villes"""

    def __init__(self, tail, head, prix, moyen, temps):
        super().__init__(tail, head)
        self.prix = prix
        self.moyen = moyen
        self.temps = temps


def short_path(start_node, end_node, weight_func=lambda edge: 1):
    """Calcule le plus court chemin entre deux noeuds d'un graph
    Une Node représete un point contenant une liste d'arêtes sortantes (out_edges)
    Un Edge représete une arête entre deux noeuds (head et tail qui sont des Nodes)
    Arguments:
        start_node: Node
        end_node: Node
        weight_func: fonction qui calcule le poids d'une arête
    retourne:
        une liste de noeuds qui représente le plus court chemin entre les deux noeuds
    """
    shortest_paths = {start_node: (0, None)}

    edge_heap = []  # Ma heap de edges
    for edge in start_node.out_edges:  # Pour chaque edge de start_node
        heappush(edge_heap, (weight_func(edge), edge))  # Ajoute l'edge dans la heap avec son poids

    while edge_heap:  # Tant que la heap n'est pas vide
        path_weight, edge = heappop(edge_heap)  # On prend le poids du plus petit edge et on le retire de la heap
        if (edge.head not in shortest_paths) or (shortest_paths[edge.head][0] > path_weight):
            shortest_paths[edge.head] = (path_weight, edge)
            for out_edge in edge.head.out_edges:
                heappush(edge_heap, (path_weight + weight_func(out_edge), out_edge))
    if end_node not in shortest_paths:
        err = ("No connection from node %s" % str(start_node) + " to node %s." % str(end_node))
        raise NoPathGraphException(err)
    path_weight = shortest_paths[end_node][0]
    path_edges = [shortest_paths[end_node][1]]
    current_node = path_edges[-1].tail
    while current_node is not start_node:
        path_edges.append(shortest_paths[current_node][1])
        current_node = path_edges[-1].tail
    # list[start:end:step]
    return path_edges[::-1], path_weight


