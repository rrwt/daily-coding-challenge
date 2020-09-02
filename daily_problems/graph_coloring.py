"""
Given an undirected graph with maximum degree D,
find a legal graph coloring using at most D+1 colors.

A graph coloring is when you assign colors to each node in a graph.
A legal coloring means no adjacent nodes have the same color

Edge coloring is less common, but it's also a thing.
A legal edge coloring means no nodes have two edges with the same color.

The lowest number of colors we can use to legally color a graph is called the chromatic number.
There's no known polynomial time solution for finding a graph’s chromatic number.
It might be impossible, or maybe we just haven’t figured out a solution yet.
We can't even determine in polynomial time if a graph can be colored using a given kkk colors.
Even if k is as low as 3.
We care about polynomial time solutions (n raised to a constant power,
like O(n^2) because for large n, polynomial time algorithms are more practical
to actually use than higher runtimes like exponential time
(a constant raised to the power of n, like O(2^n). Computer scientists usually
call algorithms with polynomial time solutions feasible, and problems with worse
runtimes intractable.
The problem of determining if a graph can be colored with k colors is in the class
of problems called NP (nondeterministic polynomial time). This means that in polynomial time,
we can verify a solution is correct but we can’t come up with a solution. In this case,
if we have a graph that's already colored with kkk colors we verify the coloring uses k colors
and is legal, but we can't take a graph and a number kkk and determine if the graph can be
colored with k colors.
For coloring a graph using as few colors as possible, we don’t have a feasible solution.
For real-world problems, we'd often need to check so many possibilities that we’ll never
be able to use brute-force no matter how advanced our computers become.
One way to reliably reduce the number of colors we use is to use the greedy algorithm
but carefully order the nodes. For example, we can prioritize nodes based on their degree,
the number of colored neighbors they have, or the number of uniquely colored neighbors they have
"""
from typing import List


def legal_graph_coloring(graph: List[List[int]], num_vertices: int, max_degree: int) -> List[int]:
    """
    Each node has at most D neighbors, and we have D+1 colors.
    So, if we look at any node, there's always at least one color that's not taken by its neighbors.
    So D+1 is always enough colors for a legal coloring.

    Time Complexity: O(num_vertices + num_edges)
    Space Complexity: O(max_degree)
    """
    all_colors = list(range(1, max_degree + 2))
    colored_vertices = [0] * num_vertices

    for vertex in range(num_vertices):
        neighboring_colors = set()

        for neighbor, connected in enumerate(graph[vertex]):
            if connected:
                neighboring_colors.add(colored_vertices[neighbor])

        for color in all_colors:
            if color not in neighboring_colors:
                colored_vertices[vertex] = color
                break
        else:
            raise AssertionError("Cannot color the graph")

    return colored_vertices


if __name__ == "__main__":
    print(
        legal_graph_coloring(
            [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0]], 4, 3
        )
    )
