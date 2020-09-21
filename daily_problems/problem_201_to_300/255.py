"""
The transitive closure of a graph is a measure of which vertices
are reachable from other vertices. It can be represented as a matrix M,
where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.
For example, suppose we are given the following graph in adjacency list form:
    graph = [ [0, 1, 3], [1, 2], [2], [3] ]
The transitive closure of this graph would be:
    [1, 1, 1, 1]
    [0, 1, 1, 0]
    [0, 0, 1, 0]
    [0, 0, 0, 1]

Given a graph, find its transitive closure.
"""
from typing import List


def dfs(graph: List[List[int]], src: int, dst: int, t_closure: List[List[int]]) -> None:
    t_closure[src][dst] = 1

    for conn in graph[dst]:
        if t_closure[src][conn] == 0:
            dfs(graph, src, conn, t_closure)


def transitive_closure(graph: List[List[int]]) -> List[List[int]]:
    size = len(graph)
    t_closure = [[0] * size for _ in range(size)]

    for src in range(size):
        dfs(graph, src, src, t_closure)

    return t_closure


if __name__ == "__main__":
    assert transitive_closure([[0, 1, 3], [1, 2], [2], [3]]) == [
        [1, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
