"""
Recall that the minimum spanning tree is the subset of edges of a tree
that connect all its vertices with the smallest possible total edge weight.
Given an undirected graph with weighted edges,
compute the maximum weight spanning tree.
"""
import sys
from typing import List, Tuple


def gen_graph_from_adjacency_matrix(graph) -> List[Tuple[int, ...]]:
    res = []

    for src, conn in enumerate(graph):
        for dst, weight in enumerate(conn):
            if 0 < weight < sys.maxsize:
                res.append((src, dst, weight))

    return res


class KruskalMST:  # maximum spanning tree
    def __init__(self, graph: List[List[int]], vertices: int) -> None:
        self.graph = gen_graph_from_adjacency_matrix(graph)
        self.vertices = vertices
        self.parent = [0] * self.vertices
        self.rank = [0] * self.vertices

        for node in range(self.vertices):
            self.parent[node] = node

    def sorted_edges(self):
        # sort by decreasing weight
        return sorted(self.graph, key=lambda item: item[2], reverse=True)

    def union(self, first: int, second: int) -> None:
        parent_first = self.parent[first]
        parent_second = self.parent[second]
        rank_first = self.rank[parent_first]
        rank_second = self.rank[parent_second]

        if rank_first > rank_second:
            self.parent[parent_second] = parent_first
        elif rank_second > rank_first:
            self.parent[parent_first] = parent_second
        else:
            self.parent[parent_second] = parent_first
            self.rank[parent_first] += 1

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def get_mst(self) -> List[Tuple[int, ...]]:
        """
        Add an edge iff
            - it is the next most weighted edge
            - it does not form a cycle with existing mst
        """
        mst = []
        edges = 0

        for src, dst, weight in self.sorted_edges():
            parent_src = self.find(src)
            parent_dst = self.find(dst)

            if parent_src != parent_dst:
                self.union(parent_src, parent_dst)
                edges += 1
                mst.append((src, dst, weight))

                if edges == self.vertices - 1:
                    break

        return mst


if __name__ == "__main__":
    max_st = KruskalMST([[0, 10, 6, 5], [10, 0, 0, 15], [6, 0, 0, 4], [5, 15, 5, 0]], 4)
    assert sum(tup[2] for tup in max_st.get_mst()) == 31
