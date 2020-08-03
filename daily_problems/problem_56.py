"""
Given an undirected graph represented as an adjacency matrix and an integer k,
write a function to determine whether each vertex in the graph can be colored
such that no two adjacent vertices share the same color using at most k colors.
"""
from collections import deque
from typing import List


# Might not work.
# I haven't tested it extensively.
# Alternate Solution: Count max number of edges for any node. k should be >= num_edges + 1
def can_color_graph(graph: List[List[int]], num_vertices: int, k: int) -> bool:
    """
    BFS along with keeping track of adjacent vertices and their color
    """
    color_arr = [-1] * num_vertices
    queue = deque([0])
    visited = set()
    next_color = 0
    color_arr[0] = next_color
    visited.add(0)

    while queue:
        node = queue.popleft()

        for neighbor, connected in enumerate(graph[node]):
            if connected == 0:
                continue
            if color_arr[neighbor] == color_arr[node]:
                return False
            if color_arr[neighbor] == -1:
                next_color = (next_color + 1) % k
                if next_color == color_arr[node]:
                    next_color = (next_color + 1) % k

                color_arr[neighbor] = next_color

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False if -1 in color_arr else True


if __name__ == "__main__":
    assert can_color_graph([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], 4, 4) is True
    assert can_color_graph([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]], 4, 3) is False
