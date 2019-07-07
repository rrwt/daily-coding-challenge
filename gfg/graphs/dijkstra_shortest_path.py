"""
Dijkstra's Shortest Path Algorithm
Greedy. Similar to Prim's MST.

Given a graph and a source vertex, find the distance to all vertices from this vertex.
"""
import sys
from typing import Tuple

from ds import GraphM  # type: ignore


def next_min(sp_set: set, distance: list) -> Tuple[int, int]:
    """
    Get the next min distant element
    """
    min_dist = sys.maxsize
    index = 0

    for vertex, d in enumerate(distance):
        if vertex not in sp_set and d < min_dist:
            min_dist = d
            index = vertex

    return index, min_dist


def dijsktra_sp(graph: list, source: int, vertices: int) -> list:
    """
    Greedily pick connected elements with minimum distance/weight
    from the given set of unconnected vertices and add them to resulting tree.
    Time complexity: O(V*V)
    """
    sp_set: set = set()
    distance: list = [sys.maxsize for _ in range(vertices)]
    distance[source] = 0
    parent: list = [None] * vertices  # only if path is important

    while len(sp_set) < vertices:
        next_el, next_dist = next_min(sp_set, distance)
        distance[next_el] = next_dist
        sp_set.add(next_el)

        for vertex, dist in enumerate(graph[next_el]):
            if vertex not in sp_set and distance[vertex] > dist + next_dist:
                distance[vertex] = dist + next_dist
                parent[vertex] = next_el

    for i in range(vertices):
        if parent[i] is not None:
            print(parent[i], "->", i, ":", distance[i])

    return distance


if __name__ == "__main__":
    graph = GraphM(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    print(dijsktra_sp(graph.graph, 0, graph.num_vertices))
