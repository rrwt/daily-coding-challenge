"""
Depth first search traversal of an undirected graph
"""
import math

from gfg.graphs.ds import GraphM  # type: ignore


def depth_first_traversal(graph: list, first_node: int) -> None:
    """
    Time complexity: O(V+E)
    Space complexity: O(V)
    """
    if graph:
        stack: list = []
        visited: set = set()
        stack.append(first_node)
        visited.add(first_node)

        while stack:
            node = stack.pop()
            print(node, end=" ")

            for element, connection in enumerate(graph[node]):
                if connection and element not in visited and connection < math.inf:
                    stack.append(element)
                    visited.add(element)


if __name__ == "__main__":
    g = GraphM(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    print("dfs starting at node 2")
    depth_first_traversal(g.graph, 2)
    print()
    print("dfs starting at node 1")
    depth_first_traversal(g.graph, 1)
    print()
    print("dfs starting at node 0")
    depth_first_traversal(g.graph, 0)
    print()
    print("dfs starting at node 3")
    depth_first_traversal(g.graph, 3)
    print()
