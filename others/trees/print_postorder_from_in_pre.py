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


if __name__ == "__main__":
    print_postorder([4, 2, 5, 1, 3, 6], [1, 2, 4, 5, 3, 6], 6)
    print()
