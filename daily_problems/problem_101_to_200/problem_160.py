"""
Given a tree where each edge has a weight, compute the length of the longest path in the tree.
For example, given the following tree:
   a
  /|\
 b c d
    / \
   e   f
  / \
 g   h

and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1,
the longest path would be c -> a -> d -> f, with a length of 17.
The path does not have to pass through the root, and each node can have any amount of children.
"""


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.children = []


def _longest_path(cur_node: Node) -> [int, int]:
    """
    Two cases arise:
    1. Longest path considering current node.
    2. Longest path leaving current node aside.
    :returns:
        Max size taking cur node or a child as root,
        Max size taking it as part of another path
    """
    if not cur_node or not cur_node.children:
        return 0, 0

    children_paths = []
    max_as_path = 0
    max_as_path_2 = 0

    for (node, dist) in cur_node.children:
        as_root, as_node = _longest_path(node)
        children_paths.append(as_root)

        if as_node + dist > max_as_path:
            max_as_path, max_as_path_2 = as_node + dist, max_as_path
        elif as_node + dist > max_as_path_2:
            max_as_path_2 = as_node + dist

    return max(max(children_paths), max_as_path_2 + max_as_path), max_as_path


def longest_path(cur_node: Node) -> int:
    return max(_longest_path(cur_node))


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.children.extend([(b, 3), (c, 5), (d, 8)])
    d.children.extend([(e, 2), (f, 4)])
    e.children.extend([(g, 1), (h, 1)])
    assert longest_path(a) == 17
