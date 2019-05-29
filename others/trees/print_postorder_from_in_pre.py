"""
Given an inorder and preorder traversal of a binary tree. Print postorder traversal
"""
from contextlib import suppress


def print_postorder(inorder: list, preorder: list, length: int):
    """
    Algorithm:
        1. First element of preorder and last of postorder is root. Print it last.
        2. Find the first element in preorder in inorder to get left and right subtree from that.
        3. Repeat
    
    time: O(n*n). getting root index is O(n). rest of the algorithm is O(n)
    space: O(n). Stack size for recursion depends on n.
    """
    root = preorder[0]
    root_index = inorder.index(root)  # guaranteed to exist in both

    if root_index > 0:  # there is a left subtree. Print it before root
        print_postorder(inorder[:root_index], preorder[1 : root_index + 1], root_index)
    if root_index < length - 1:  # there is a right subtree. Print it
        print_postorder(
            inorder[root_index + 1 :],
            preorder[root_index + 1 :],
            length - root_index - 1,
        )

    print(root, end=" ")


def print_postorder_optimised(inorder: list, preorder: list):
    """
    Using extra O(n) space, this could be optimized for searchin the root index in inorder array
    time: O(n)
    space: O(n)
    """

    def postorder(start: int, end: int):
        nonlocal pre_index

        if start > end:
            return None

        root = preorder[pre_index]
        pre_index += 1
        root_index = hashmap[root]

        if root_index > start:  # left
            postorder(start, root_index - 1)
        if root_index < end:  # right
            postorder(root_index + 1, end)

        print(root, end=" ")

    hashmap = {v: k for k, v in enumerate(inorder)}
    pre_index = 0
    postorder(0, len(inorder) - 1)


if __name__ == "__main__":
    print_postorder([4, 2, 5, 1, 3, 6], [1, 2, 4, 5, 3, 6], 6)
    print()
    print_postorder_optimised([4, 2, 5, 1, 3, 6], [1, 2, 4, 5, 3, 6])
    print()
