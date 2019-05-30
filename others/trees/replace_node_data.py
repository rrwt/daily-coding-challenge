"""
Given a binary tree containing n nodes. The problem is to replace each node in
the binary tree with the sum of its inorder predecessor and inorder successor.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def replace_data(root: Node) -> Node:
    """
    Traverse inorder, create an aux array.
    Traverse inorder again and replace data, taking it from aux array
    time complexity: O(n)
    space complexity: O(n)
    """

    def traverse_inorder(node, fill_array):
        nonlocal in_iter

        if not node:
            return None

        traverse_inorder(node.left, fill_array)

        if fill_array:
            arr.append(node.data)
        else:
            if in_iter == 0:
                node.data = arr[1]
            elif in_iter == l - 1:
                node.data = arr[l - 2]
            else:
                node.data = arr[in_iter - 1] + arr[in_iter + 1]
            in_iter += 1

        traverse_inorder(node.right, fill_array)

    arr: list = []
    traverse_inorder(root, fill_array=True)
    in_iter = 0
    l = len(arr)
    traverse_inorder(root, fill_array=False)
    return root


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(inorder(root))
    root = replace_data(root)
    print(inorder(root))
