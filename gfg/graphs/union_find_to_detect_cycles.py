"""
Union-Find algorithm to detect circles in a graph

Union: Join two subsets.  O(n)
Find: Detect if two nodes have same parent node.  O(n)

Union by rank: Attach tree with smaller depth as a subtree of one with larger. O(log(n))
Find by path compression: At every find recursion, mark parent of all as parent of current. O(log(n))
"""
from dataclasses import dataclass

from ds import GraphM  # type: ignore


def union(v1: int, v2: int, subsets: list):
    pv1 = subsets[v1].parent
    pv2 = subsets[v2].parent

    if pv1 == pv2:
        return

    if subsets[pv1].rank > subsets[pv2].rank:
        subsets[pv2].parent = pv1
    elif subsets[pv1].rank < subsets[pv2].rank:
        subsets[pv1].parent = pv2
    else:
        subsets[pv1].parent = pv2
        subsets[pv2].rank += 1


def find(vertex: int, subset: list) -> int:
    if subset[vertex].parent != vertex:
        subset[vertex].parent = find(subset[vertex].parent, subset)
    return subset[vertex].parent


@dataclass
class Subset:
    parent: int
    rank: int


def is_cyclic(graph: list, vertices: int) -> bool:
    subsets: list = [Subset(v, 0) for v in range(vertices)]

    for u in range(len(graph)):
        pu = find(u, subsets)

        for v, connection in enumerate(graph[u]):
            if u != v and connection == 1:
                pv = find(v, subsets)

                if pu == pv:
                    return True
                union(pu, pv, subsets)
    return False


if __name__ == "__main__":
    g = GraphM(3, "directed")
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)

    if is_cyclic(g.graph, g.num_vertices):
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")

