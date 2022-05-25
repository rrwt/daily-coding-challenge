"""
Detect Cycle in a directed graph
"""
import math

from gfg.graphs.ds import GraphM  # type: ignore


def print_cycle(start: int, end: int, stack: list) -> None:
    start_index = stack.index(start)

    print(f"Cycle detected from {start} to {end}")

    while start_index < len(stack) - 1:
        print(stack[start_index], end="->")
        start_index += 1

    print(end)


def dfs(graph: list, vertex: int, cur_stack: list, visited: set, processed: set) -> bool:
    cycle = False

    if vertex not in processed:
        new_stack = cur_stack + [vertex]

        for neighbor, cost in enumerate(graph[vertex]):
            if 0 < cost < math.inf:
                if neighbor in visited:
                    print_cycle(neighbor, vertex, new_stack)
                    processed.add(neighbor)  # cycle starting from this point
                    return True
                else:
                    cycle = dfs(graph, neighbor, new_stack, visited.union({neighbor}), processed)

            if cycle:
                return cycle

    return cycle


def detect_cycle_dfs(graph: list, vertices: int) -> None:
    processed = set()

    for vertex in range(vertices):
        dfs(graph, vertex, [], set(), processed)


def detect_print_cycle(graph: list, vertices: int) -> None:
    """
    initial set - List of unvisited nodes
    Gray set - List of nodes being visited
    processed set - List of completely visited nodes (Node and Children)
    Parent map - key: value where key is immediate child and value is immediate parent
    """
    initial_set: set = set(_ for _ in range(vertices))
    gray_stack: list = []
    gray_set: set = set()
    processed_set: set = set()
    parent_map: dict = {}

    while initial_set or gray_stack:
        explored: bool = True
        if gray_stack:
            cur_node = gray_stack.pop()

            for neighbor, conn in enumerate(graph[cur_node]):
                if neighbor not in processed_set and 0 < conn < math.inf:
                    # only work if the subtree is not completely visited and there is a connection
                    explored = False
                    parent_map[neighbor] = cur_node

                    if neighbor in gray_set:
                        print(f"Cycle Found from {neighbor} to {cur_node}")
                    else:
                        gray_stack.append(neighbor)
                        gray_set.add(neighbor)
                        initial_set.remove(neighbor)

            if explored:  # if sub-graph is completely explored, move the node to processed
                gray_set.remove(cur_node)
                processed_set.add(cur_node)
        else:
            cur_node = initial_set.pop()
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
    detect_cycle_dfs(g.graph, g.num_vertices)

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
    detect_cycle_dfs(g.graph, g.num_vertices)
