import math
from collections import defaultdict, deque

from ds import GraphM  # type: ignore


def topological_sort_using_dfs(graph: list, vertices: int) -> list:
    """
    Graph must be a DAG. No need to verify for existing elements
    Time complexity: O(V+E)
    Space complexity: O(V)
    """

    def dfs(index):
        nonlocal visited

        visited.add(index)

        for vertex, connected in enumerate(graph[index]):
            if connected == 1 and vertex not in visited:
                dfs(vertex)

        stack.append(index)

    visited: set = set()
    stack: list = []

    for index in range(vertices):
        if index not in visited:
            dfs(index)

    return stack[::-1]


def topological_sort_kahn_algorithm(graph: list, vertices: int) -> list:
    """
    time complexity: O(V+E)

    1. Get in-degree of every node
    2. Pick all the vertices with in-degree as 0 and add them into a queue
    3. Remove a vertex from the queue (Dequeue operation) and then.
        Increment count of visited nodes by 1.
        Decrease in-degree by 1 for all its neighboring nodes.
        If in-degree of a neighboring nodes is reduced to zero, then add it to the queue.
    4. Repeat Step 3 until the queue is empty.
    5.  If count of visited nodes is not equal to the number of nodes in the graph then the
        topological sort is not possible for the given graph.
    """

    def get_indegrees():
        indegree: list = [0] * vertices

        for i in range(vertices):
            for vertex, connected in enumerate(graph[i]):
                indegree[vertex] += 1 if connected == 1 else 0

        return indegree

    def create_queue(indegree):
        queue: deque = deque()

        for vertex, degree in enumerate(indegree):
            if degree == 0:
                queue.append(vertex)

        return queue

    indegree_list: list = get_indegrees()
    queue: deque = create_queue(indegree_list)
    visited: set = set()
    ts_list: list = []

    while queue:
        element = queue.popleft()
        ts_list.append(element)
        visited.add(element)

        for vertex, connected in enumerate(graph[element]):
            if connected == 1:
                indegree_list[vertex] -= 1

                if indegree_list[vertex] == 0:
                    queue.append(vertex)

    return ts_list if len(visited) == len(graph) else []


if __name__ == "__main__":
    g = GraphM(7, "directed")
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    print(topological_sort_using_dfs(g.graph, g.num_vertices))
    print(topological_sort_kahn_algorithm(g.graph, g.num_vertices))
