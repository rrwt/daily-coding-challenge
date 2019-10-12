"""
Detect Cycle in a directed graph
"""
import math

from ds import GraphM  # type: ignore


def detect_print_cycle(graph: list, vertices: int) -> bool:
    """
    White set - List of unvisited nodes
    Gray set - List of nodes being visited
    Black set - List of completely visited nodes (Node and Children)
    Parent map - key: value where key is immediate child and value is immediate parent
    """
    white_set: set = set(_ for _ in range(vertices))
    gray_stack: list = []
    gray_set: set = set()
    black_set: set = set()
    parent_map: dict = {}

    while white_set or gray_stack:
        found: bool = False
        if gray_stack:
            cur_node = gray_stack.pop()

            for neighbor, conn in enumerate(graph[cur_node]):
                if neighbor not in black_set and 0 < conn < math.inf:
                    # only work if the subtree is not completely visited and there is a connection
                    found = True
                    parent_map[neighbor] = cur_node

                    if neighbor in gray_set:
                        print(f"Cycle Found from {neighbor} to {cur_node}")
                    else:
                        gray_stack.append(neighbor)
                        gray_set.add(neighbor)
                        white_set.remove(neighbor)

            if not found:  # if subgraph is completely explored, move the node to black
                gray_set.remove(cur_node)
                black_set.add(cur_node)
        else:
            while gray_set:
                black_set.add(gray_set.pop())

            cur_node = white_set.pop()
            gray_set.add(cur_node)
            gray_stack.append(cur_node)


if __name__ == "__main__":
    g = GraphM(4, "directed")
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("First Graph")
    for i in range(g.num_vertices):
        print(g.graph[i])

    detect_print_cycle(g.graph, g.num_vertices)

    g = GraphM(6, "directed")
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 3)

    print("Second Graph")
    for i in range(g.num_vertices):
        print(g.graph[i])

    detect_print_cycle(g.graph, g.num_vertices)
