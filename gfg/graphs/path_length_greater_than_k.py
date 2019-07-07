"""
Given a graph, a source vertex in the graph and a number k,
find if there is a simple path (without any cycle) starting
from given source and ending at any other vertex.
"""
import math

from ds import GraphM  # type: ignore


def path(graph: list, source: int, k: int, vertices: int) -> list:
    """
    Greedy solution won't always work. We'd need to try every possible
    path from source to all other vertices.
    Backtracking should be applied here.
    Time Complexity: O(n!)
    """

    def backtrack(next_vertex: int, distance: int, visited: set, total: int) -> int:
        nonlocal path

        if next_vertex in visited:
            return 0

        visited.add(next_vertex)
        path.append(next_vertex)
        cur_total = total + distance

        if cur_total > k:
            return cur_total

        for vertex, dist in enumerate(graph[next_vertex]):
            if vertex not in visited and 0 < dist < math.inf:
                cur_total = backtrack(vertex, dist, visited, cur_total)

                if cur_total > k:
                    return cur_total

        visited.remove(next_vertex)
        path.pop(-1)
        return total

    path: list = [source]

    for vertex, distance in enumerate(graph[source]):
        if 0 < distance < math.inf and backtrack(vertex, distance, {source}, 0) > k:
            return path

    return []


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

    print(path(graph.graph, 0, 60, graph.num_vertices))
