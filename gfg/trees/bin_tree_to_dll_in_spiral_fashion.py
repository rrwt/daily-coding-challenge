"""
Given a Binary Tree, convert it into Doubly Linked List where the nodes are
represented Spirally. The left pointer of the binary tree node should act as
a previous node for created DLL and right pointer should act as next node.
The solution should not allocate extra memory for DLL nodes. It should use
binary tree nodes for creating DLL i.e. only change of pointers is allowed
"""
from collections import deque
from typing import Optional

from binary_tree_node import Node  # type: ignore


def convert_to_dll(root: Optional[Node]) -> Optional[Node]:
    if root is None:
        return None

    queue = deque()
    stack = []
    queue.append(root)
    direction = True

    while queue:
        length = len(queue)

        if direction:
            while length:
                node = queue.pop()
                stack.append(node)

                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)
                length -= 1
        else:
            while length:
                node = queue.popleft()
                stack.append(node)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)
                length -= 1

        direction = not direction

    head = stack.pop()

    while stack:
        node = stack.pop()
        head.left = node
        node.right = head
        head = node

    return head


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
    root.right.right.right = Node(14)
    head = convert_to_dll(root)
    while head and head.right:
        print(head.data, end="->")
        head = head.right
    print(head.data)
