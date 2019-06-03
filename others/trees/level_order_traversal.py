"""
Level order traversal is also called breadth first traversal
"""
from collections import deque

from binary_tree_node import Node  # type: ignore


def level_order_using_extra_space(root: Node):
    """
    Using a queue
    time complexity: O(n)
    space complexity: O(n)
    """
    queue: deque = deque()

    while queue or root:
        print(root.data, end=" ")

        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

        root = queue.popleft() if queue else None


def get_height(root: Node) -> int:
    if not root:
        return 0
    else:
        left = get_height(root.left)
        right = get_height(root.right)
        return max(left, right) + 1


def get_nodes_at_height(root: Node, height: int):
    if root and height == 1:
        print(root.data, end=" ")
    elif height > 1:
        get_nodes_at_height(root.left, height - 1)
        get_nodes_at_height(root.right, height - 1)


def level_order_recursive(root: Node):
    height: int = get_height(root)

    for i in range(1, height + 1):
        get_nodes_at_height(root, i)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(5)

    level_order_using_extra_space(root)
    print()
    level_order_recursive(root)
    print()
