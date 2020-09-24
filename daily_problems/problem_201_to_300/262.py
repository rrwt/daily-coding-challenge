"""
A bridge in a connected (undirected) graph is an edge that, if removed,
causes the graph to become disconnected. Find all the bridges in a graph.
"""
from typing import Tuple, List, Set


def dfs(graph: List[List[int]], src: int, visited: set) -> set:
    visited.add(src)

    for dst, conn in enumerate(graph[src]):
        if conn == 1 and dst not in visited:
            dfs(graph, dst, visited)

    return visited


def get_bridges(graph: List[List[int]]) -> Set[Tuple[int, int]]:
    size = len(graph)
    res = set()

    for src in range(size):
        for dst, conn in enumerate(graph[src]):
            if conn == 1 and (dst, src) not in res:
                graph[src][dst] = 0
                visited = dfs(graph, src, set())

                if len(visited) < size:
                    res.add((src, dst))

                graph[src][dst] = 1

    return res


if __name__ == "__main__":
    assert get_bridges(
        [
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
        ]
    ) == {(3, 4), (0, 3)}

    assert get_bridges([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]) == {
        (2, 3),
        (0, 1),
        (1, 2),
    }
