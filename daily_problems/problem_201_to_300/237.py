"""
A tree is symmetric if its data and shape remain unchanged when
it is reflected about the root node. The following tree is an example:
        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.children = []


def tree_is_symmetric(root_1: Node, root_2: Node) -> bool:
    if not (root_1 or root_2):
        return True
    if not (root_1 and root_2):
        return False

    if len(root_1.children) != len(root_2.children) or root_1.data != root_2.data:
        return False

    size = len(root_1.children)

    for index in range(size):
        is_sym = tree_is_symmetric(
            root_1.children[index], root_2.children[size - index - 1]
        )
        if not is_sym:
            return False

    return True


if __name__ == "__main__":
    root = Node(4)
    root.children.extend([Node(3), Node(5), Node(3)])
    root.children[0].children.append(Node(9))
    root.children[2].children.append(Node(9))
    assert tree_is_symmetric(root, root) is True

    root = Node(1)
    root.children = [Node(2), Node(3), Node(2)]
    root.children[0].children = [Node(4), Node(5)]
    root.children[1].children = [Node(6)]
    root.children[2].children = [Node(5), Node(4)]
    assert tree_is_symmetric(root, root) is True

    root.children[0].children[0].children = [Node(7)]
    assert tree_is_symmetric(root, root) is False
