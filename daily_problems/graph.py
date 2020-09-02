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
