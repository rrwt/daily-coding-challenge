"""
Find postorder traversal of given Binary Search Tree, given it's preorder traversal
"""
from typing import Optional


def postorder(preorder: list, length: int, res: Optional[list] = None) -> list:
    """
    BST: all elements with value less than the root are part of left subtree and
        all with value greater than root are part of right subtree
    time complexity: O(n*n)  # TODO
    space complexity: O(n)  # stack
    """

    if res is None:
        res = []

    root = preorder[0]
    last_left_index = 0

    for i in range(1, length):
        if preorder[i] < root:
            last_left_index = i
        else:
            break

    if last_left_index > 0:  # left subtree
        res.extend(postorder(preorder[1 : last_left_index + 1], last_left_index))
    if last_left_index < length - 1:
        res.extend(
            postorder(preorder[last_left_index + 1 :], length - last_left_index - 1)
        )

    res.append(root)

    return res


if __name__ == "__main__":
    assert postorder([40, 30, 35, 80, 100], 5) == [35, 30, 100, 80, 40]
