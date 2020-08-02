"""
Given a graph and a source vertex src in graph,
find shortest paths from src to all vertices in the given graph.
The graph may contain negative weight edges.

Dijkstra does not work for Graphs with negative weight edges,
Bellman-Ford works for such graphs.
Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems.
But time complexity of Bellman-Ford is O(VE) - adjacency list, which is more than Dijkstra.

If there is a negative weight cycle, then shortest distances are not calculated,
negative weight cycle is reported.
"""
import sys

from gfg.graphs.ds import GraphM


def bellman_ford_sp(graph: list, source: int, num_vertices: int) -> list:
    """
    Time Complexity: O(V*V*E)  (O(V*E) for adjacency list)
    """
    distance = [sys.maxsize] * num_vertices
    distance[source] = 0

    # calculate distance. BFS
    for _ in range(num_vertices-1):
        for src in range(num_vertices):
            if distance[src] < sys.maxsize:
                for dest, weight in enumerate(graph[src]):
                    if weight < sys.maxsize:
                        distance[dest] = min(distance[dest], weight + distance[src])

    # check for -ve cycle
    for src in range(num_vertices):
        for dest, dist in enumerate(graph[src]):
            if src == dest:
                continue
            if graph[src][dest] < sys.maxsize and distance[dest] > distance[src] + dist:
                print("-ve cycle found")
                return []

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

    print(bellman_ford_sp(g.graph, 0, g.num_vertices))

    g.add_edge(2, 4, -1)
    print(bellman_ford_sp(g.graph, 0, g.num_vertices))
