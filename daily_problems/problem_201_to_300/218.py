"""
Write an algorithm that computes the reversal of a directed graph.
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""
from typing import List


def transpose_directed_graph(
    graph: List[List[int]], num_vertices: int
) -> List[List[int]]:
    visited_edges = set()

    for src in range(num_vertices):
        for dst, conn in enumerate(graph[src]):
            if (
                conn
                and (dst, src) not in visited_edges
                and (src, dst) not in visited_edges
            ):
                visited_edges.add((src, dst))
                graph[dst][src] = 1
                graph[src][dst] = 0

    return graph


if __name__ == "__main__":
    g = [
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
    ]
    print(g)
    print(transpose_directed_graph(g, 5))
