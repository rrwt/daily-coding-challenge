"""
Prim's Minimum Spanning Tree algorithm.
Prefer this when the graph is dense.
"""
import math

from gfg.graphs.ds import GraphM  # type: ignore


def get_min_weight_index(weights: list, mst_set: set) -> int:
    """
    Get next min weight node greedily. O(V)
    """
    min_weight = math.inf
    index = 0

    for i in range(len(weights)):
        if weights[i] < min_weight and i not in mst_set:
            min_weight = weights[i]
            index = i

    return index


def update_weight(graph: list, vertex: int, mst_set: set, weights: list, parent: list):
    """
    Update the weight array (distance) for all neighbours
    """
    for i in range(len(graph)):
        if 0 < graph[vertex][i] < weights[i] and i not in mst_set:
            weights[i] = graph[vertex][i]
            parent[i] = vertex


def prim_mst(graph: list, vertices: int) -> None:
    """
    Create a set mst_set that keeps track of vertices already included in MST.
    Assign a key value to all vertices in the input graph.
        Initialize all key values as INFINITE.
        Assign key value as 0 for the first vertex so that it is picked first.
    While mst_set does not include all vertices
        Pick a vertex u which is not there in mst_set and has minimum key value.
        Include u to mst_set.
        Update key value of all adjacent vertices of u. To update the key values,
        iterate through all adjacent vertices. For every adjacent vertex v,
        if weight of edge u-v is less than the previous key value of v,
        update the key value as weight of u-v

    Time Complexity: O(V*V) (O(E*logV) using adjacency list)
    """
    mst_set: set = set()  # keep track of visited nodes
    weights: list = [math.inf for _ in range(vertices)]  # next connected, lightest node
    weights[0] = 0
    edges = 0
    parent: list = [None] * vertices  # from node

    while edges < vertices - 1:
        next_vertex = get_min_weight_index(weights, mst_set)
        mst_set.add(next_vertex)
        update_weight(graph, next_vertex, mst_set, weights, parent)
        edges += 1

    for i in range(1, vertices):
        print(parent[i], "->", i, ":", weights[i])


if __name__ == "__main__":
    g = GraphM(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    prim_mst(g.graph, g.num_vertices)
