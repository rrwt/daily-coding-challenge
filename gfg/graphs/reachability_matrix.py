"""Directed Graph
A reachability matrix or transitive closure is the matrix defining the path from
vertex a to b for all pair of vertices (a, b).
"""


def reachability_matrix(graph: list) -> list:
    """
    DFS can be used to create it.
    time complexity: O(V*(V+E)). For a dense graph E -> V*V, then it will become O(V^3)
    space complexity: O(V)  # not counting the matrix itself, which is O(V*V)
    """

    def dfs(v1: int, v2: int):  # O(V+E)
        nonlocal dim
        matrix[v1][v2] = 1

        for i in range(dim):
            if graph[v1][i] and not matrix[v1][i]:
                matrix[v1][i] = 1
                dfs(i, i)

    dim: int = len(graph)
    matrix: list = [[0] * dim for _ in range(dim)]

    for i in range(dim):  # O(V)
        dfs(i, i)

    return matrix


if __name__ == "__main__":
    graph = [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]
    print(*reachability_matrix(graph), sep="\n")
