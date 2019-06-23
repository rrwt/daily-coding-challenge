"""
Detect Cycle in a directed graph
"""
from ds import GraphM  # type: ignore


def has_cycle(graph: list, vertices: int) -> bool:
    stack: list = []
    visited: set = set()

    stack.append(0)
    visited.add(0)

    while stack:
        element = stack.pop()

        for i in range(vertices):
            if graph[element][i] == 1:
                if i not in visited and i not in stack:
                    stack.append(i)
                    visited.add(i)
                elif i in stack:
                    return True

    return False


if __name__ == "__main__":
    g = GraphM(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    if has_cycle(g.graph, g.num_vertices):
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
