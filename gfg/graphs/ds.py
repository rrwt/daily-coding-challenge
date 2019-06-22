"""
Adjacency matrix and adjacency list representation for graph
"""
import math


def verify_vertices(func):
    def wrapper(self, v1: int, v2: int, *args, **kwargs):
        assert 0 <= v1 < self.num_vertices
        assert 0 <= v2 < self.num_vertices
        func(self, v1, v2, *args, **kwargs)

    return wrapper


class GraphM:
    """
    Using an adjacency Matrix
    V = number of vertices
    Space Complexity: O(V*V)
    Time Complexity: Verify, Remove, Add Edge -> O(1)
        Add new vertex: O(V*V) [because the data needs to be copied to a new bigger matrix]
    """

    def __init__(self, num_vertices: int, type_of_graph: str = "undirected"):
        assert type_of_graph in ("undirected", "directed")
        self.graph: list = [[math.inf] * num_vertices for _ in range(num_vertices)]
        self.num_vertices: int = num_vertices
        self.type = type_of_graph

        for v in range(self.num_vertices):
            self.graph[v][v] = 0

    @verify_vertices
    def add_edge(self, v1: int, v2: int, weight: int = 1) -> None:
        self.graph[v1][v2] = weight

        if self.type == "undirected":
            self.graph[v2][v1] = weight

    @verify_vertices
    def remove_edge(self, v1: int, v2: int) -> None:
        self.graph[v1][v2] = math.inf

        if self.type == "undirected":
            self.graph[v2][v1] = math.inf

    @verify_vertices
    def contains_edge(self, v1: int, v2: int) -> bool:
        return self.graph[v1][v2]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class GraphL:
    """
    Using an adjacency list
    Space Complexity: O(V+E), worst case: O(V*V), (full graph)
    Time complexity: Add, Delete, Query: O(V)
    """

    def __init__(self, num_vertices: int, type_of_graph: str = "undirected"):
        assert type_of_graph in ("undirected", "directed")
        self.graph: list = [None] * num_vertices
        self.num_vertices: int = num_vertices
        self.type: str = type_of_graph

    @verify_vertices
    def add_directed_edge(self, v1: int, v2: int, weight: int = 1):
        if not self.graph[v1]:
            self.graph[v1] = Node(v2)
        else:
            head = self.graph[v1]
            while head.next and head.data != v2:
                head = head.next

            if head.data != v2:
                head.next = Node(v2)

    def add_edge(self, v1: int, v2: int, weight: int = 1):
        self.add_directed_edge(v1, v2, weight)

        if self.type == "undirected":
            self.add_directed_edge(v2, v1, weight)

    @verify_vertices
    def remove_directed_edge(self, v1: int, v2: int):
        head = self.graph[v1]

        if head:
            if head.data == v2:
                self.graph[v1] = head.next
                del head
            else:
                while head.next:
                    if head.next.data == v2:
                        head.next = head.next.next
                        break
                    else:
                        head = head.next

    def remove_edge(self, v1: int, v2: int):
        self.remove_directed_edge(v1, v2)

        if self.type == "undirected":
            self.remove_directed_edge(v2, v1)
