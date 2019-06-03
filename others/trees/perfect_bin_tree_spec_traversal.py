"""
Print a perfect binary tree in level order and outside in
e.g.
1 -> 2 3 -> 4 5 6 7 -> 8 9 10 11 12 13 14 15
will print:
1 -> 2 3 -> 4 7 5 6 -> 8 15 9 14 10 13 11 12
"""
from collections import deque

from binary_tree_node import Node  # type: ignore


def specific_level_order_traversal(root: Node):
    def insert(data_node: Node, order: int = 1):
        if order == 1:
            if data_node.left:
                # in a perfect binary tree, we don't need to check both sides
                lque.append(data_node.left)
                lque.append(data_node.right)
        else:
            if data_node.right:
                rque.append(data_node.right)
                rque.append(data_node.left)

    lque: deque = deque()
    rque: deque = deque()

    lque.append(root.left)
    rque.append(root.right)

    print(root.data)

    while lque or rque:
        if lque:
            elem = lque.popleft()
            print(elem.data)
            insert(elem, 1)
        if rque:
            elem = rque.popleft()
            print(elem.data)
            insert(elem, 2)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    specific_level_order_traversal(root)
