"""
Kruskal's Minimum spanning tree
Note: for any MST: E = V-1

Prefer this when the graph is sparse and/or the weight matrix is already sorted or
can be sorted in linear time.
"""
import math
from collections import defaultdict

from gfg.graphs.ds import GraphM  # type: ignore
from gfg.graphs.union_find_to_detect_cycles import union, find, Subset  # type: ignore


def kruskal_mst(graph: list, vertices: int) -> list:
    """
    1. Find all edges and their weights
    2. Sort the edges in non-decreasing order of their weight
    3. Greedily pick all the edges one by one.
    4. Add new edges to existing MST using Union-Find algorithm(avoiding cycles)
    5. The algorithm ends when E = V - 1.
    Time Complexity: O(E*logE) when E > V and O(E*logV) when E <  V. max(E) = V*V
    Space Complexity: O(E)
    """
    weights: dict = defaultdict(set)

    for src in range(vertices):
        for dst, weight in enumerate(graph[src]):
            if 0 < weight < math.inf and (dst, src) not in weights[weight]:
                weights[weight].add((src, dst))

    edges = 0
    mst_edges: list = []
    subsets: list = [Subset(v, 0) for v in range(vertices)]

    sorted_list_by_weight = sorted(weights.items())  # O(E*log(E))
    i = 0

    while edges < vertices - 1 and i < len(weights):
        cur_weight, cur_edges = sorted_list_by_weight[i]

        for u, v in cur_edges:
            pu = find(u, subsets)
            pv = find(v, subsets)

            if pu != pv:
                union(u, v, subsets)
                mst_edges.append((u, v, cur_weight))
                edges += 1

                if edges >= vertices - 1:
                    break

        i += 1

    if edges < vertices - 1:
        print("E is less than V-1")

    return mst_edges


if __name__ == "__main__":
    g = GraphM(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 7, 8)
    g.add_edge(1, 2, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(2, 3, 7)
    g.add_edge(2, 5, 4)
    g.add_edge(2, 8, 2)
    g.add_edge(3, 4, 9)
    g.add_edge(3, 5, 14)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(6, 8, 6)
    g.add_edge(7, 8, 7)
    print(*kruskal_mst(g.graph, g.num_vertices), sep="\n")
