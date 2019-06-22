"""
Traverse a graph in a breadth first manner
"""
import math
from collections import deque

from ds import GraphM  # type: ignore


def breadth_first_travel(g: list, first_node: int):
    """
    Similar to level order traversal for tree
    """
    if g:
        visited = set()
        q: deque = deque()
        q.append(first_node)
        visited.add(first_node)

        while q:
            node = q.popleft()
            print(node, end=" ")

            for elem, connection in enumerate(g[node]):
                if elem not in visited and connection and connection < math.inf:
                    q.append(elem)
                    visited.add(elem)


if __name__ == "__main__":
    g = GraphM(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("bfs starting at node 2")
    breadth_first_travel(g.graph, 2)
    print()
    print("bfs starting at node 1")
    breadth_first_travel(g.graph, 1)
    print()
    print("bfs starting at node 0")
    breadth_first_travel(g.graph, 0)
    print()
    print("bfs starting at node 3")
    breadth_first_travel(g.graph, 3)
    print()
