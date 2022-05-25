"""
Dijkstra's Shortest Path Algorithm
Greedy. Similar to Prim's MST.

Given a graph and a source vertex, find the distance to all vertices from this vertex.
Does not work for Graphs with negative weight edges.
"""
import sys
from typing import Tuple

from gfg.graphs.ds import GraphM  # type: ignore


def next_min(sp_set: set, distance: list) -> Tuple[int, int]:
    """
    O(v)
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
    Time complexity: O((E+V)*logV) for adjacency matrix using min heap for next_min
    """
    sp_set: set = set()
    distance: list = [sys.maxsize] * vertices
    distance[source] = 0
    parent: list = [None] * vertices  # only if path is important

    while len(sp_set) < vertices:
        cur_el, cur_dist = next_min(sp_set, distance)
        sp_set.add(cur_el)

        for dest, dist in enumerate(graph[cur_el]):
            if dest not in sp_set and distance[dest] > dist + cur_dist:
                distance[dest] = dist + cur_dist
                parent[dest] = cur_el

    for i in range(vertices):
        if parent[i] is not None:
            print(parent[i], "->", i, ":", distance[i])

    return distance


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

    print(dijsktra_sp(g.graph, 0, g.num_vertices))
