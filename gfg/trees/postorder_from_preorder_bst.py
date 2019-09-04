"""
Find postorder traversal of given Binary Search Tree, given it's preorder traversal
"""
from typing import Optional


def postorder(preorder: list, length: int, res: Optional[list] = None) -> list:
    """
    BST: all elements with value less than the root are part of left subtree and
        all with value greater than root are part of right subtree
    time complexity: O(n*n)
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


def postorder_optimised(preorder: list, length: int) -> list:
    """
    Use a static index pre_index to iterate over the list items one by one
    when the loop returns, store the root item in list.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    min_val, max_val, pre_index = -1000_000, 1000_000, 0

    def postorder_helper(min_val: int, max_val: int) -> None:
        nonlocal preorder, length, pre_index, res

        if (
            pre_index >= length
            or preorder[pre_index] < min_val
            or preorder[pre_index] > max_val
        ):
            return None

        root = preorder[pre_index]
        pre_index += 1
        postorder_helper(min_val, root)
        postorder_helper(root, max_val)
        res.append(root)

    res = []
    postorder_helper(min_val, max_val)
    return res


if __name__ == "__main__":
    assert postorder([40, 30, 35, 80, 100], 5) == [35, 30, 100, 80, 40]
    assert postorder_optimised([40, 30, 35, 80, 100], 5) == [35, 30, 100, 80, 40]
