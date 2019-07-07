"""
Kruskal's Minimum spanning tree
Note: for any MST: E = V-1
"""
import math
from collections import defaultdict
from dataclasses import dataclass

from ds import GraphM  # type: ignore


def find(vertex: int, subsets: list):
    """
    O(log(V))
    """
    if subsets[vertex].parent != vertex:
        subsets[vertex].parent = find(subsets[vertex].parent, subsets)
    return subsets[vertex].parent


def union(u: int, v: int, subsets: list):
    """
    O(log(V))
    """
    pv1 = subsets[u].parent
    pv2 = subsets[v].parent

    if pv1 == pv2:
        return

    if subsets[pv1].rank > subsets[pv2].rank:
        subsets[pv2].parent = pv1
    elif subsets[pv1].rank < subsets[pv2].rank:
        subsets[pv1].parent = pv2
    else:
        subsets[pv1].parent = pv2
        subsets[pv2].rank += 1


@dataclass
class Subset:
    parent: int
    rank: int = 0


def kruskal_mst(graph: list, vertices: int) -> list:
    """
    1. Find all edges and their weights
    2. Sort the edges in non-decreasing order of their weight
    3. Greedily pick all the edges one by one.
    4. Add new edges to existing MST using Union-Find algorithm(avoiding cycles)
    5. The algorithm ends when E = V - 1.
    Time Complexity: O(ElogE) when E > V and O(ElogV) when E <  V. max(E) = V*V
    Space Complexity: O(E)
    """
    weights: dict = defaultdict(set)

    for main_vertex in range(vertices):
        for inner_vertex, weight in enumerate(graph[main_vertex]):
            if (
                0 < weight < math.inf
                and (inner_vertex, main_vertex) not in weights[weight]
            ):
                weights[weight].add((main_vertex, inner_vertex))

    edges = 0
    mst_edges: list = []
    subsets: list = [Subset(v, 0) for v in range(vertices)]

    sorted_list_by_weight = sorted(weights.items())  # O(E*log(E))
    i = 0

    while edges < vertices - 1 and i < len(weights):
        cur_weight, cur_edges = sorted_list_by_weight[i]
        i += 1

        for u, v in cur_edges:
            pu = find(u, subsets)
            pv = find(v, subsets)

            if pu != pv:
                union(u, v, subsets)
                mst_edges.append((u, v, cur_weight))
                edges += 1

                if edges >= vertices - 1:
                    break

    if edges < vertices - 1:
        print("E is less than V-1")

    return mst_edges


if __name__ == "__main__":
    graph = GraphM(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    print(*kruskal_mst(graph.graph, graph.num_vertices), sep="\n")
