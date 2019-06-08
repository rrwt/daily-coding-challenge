"""
Construct a special tree from given preorder traversal

Given an array ‘pre[]’ that represents Preorder traversal of a special binary tree
where every node has either 0 or 2 children. One more array ‘preLN[]’ is given
which has only two possible values ‘L’ and ‘N’. The value ‘L’ in ‘preLN[]’
indicates that the corresponding node in Binary Tree is a leaf node and value ‘N’
indicates that the corresponding node is non-leaf node.

Write a function to construct the tree from the given two arrays.
"""
from typing import Optional

from binary_tree_node import Node  # type: ignore
from depth_first_traversal_recursive import inorder  # type: ignore


def special_tree(preorder: list, pre_ln: list) -> Optional[Node]:
    """
    Facts:
        1. Full binary tree i.e. 0 or 2 children
        2. pre_ln will indicate whether the node has children
    
    time complexity: O(n)
    space complexity: O(n)  # stack
    """

    def tree() -> Optional[Node]:
        nonlocal index

        if index >= l:
            return None

        node = Node(preorder[index])
        index += 1

        if pre_ln[index - 1] == "N":
            node.left = tree()
            node.right = tree()

        return node

    index: int = 0
    l: int = len(preorder)
    return tree()


if __name__ == "__main__":
    print(inorder(special_tree([10, 30, 20, 5, 15], ["N", "N", "L", "L", "L"])))

