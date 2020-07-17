"""
Given a Singly Linked List which has data members sorted in ascending order.
Construct a Balanced Binary Search Tree which has same data members as the given Linked List. 
Balanced BST: A bst with max height difference between the left and the
    right subtree is 1 reecursively.
"""
from typing import Optional

from gfg.bst.bst_and_node import Node, inorder  # type: ignore


def create_balanced_bst(ll: list) -> Node:
    """
    Fact: Number of nodes in left and right half should be roughly n/2
    Time complexity: O(n)
    Space complexity: O(n)  # stack
    """

    def balanced_bst(n: int) -> Optional[Node]:
        """
        This implementation constructs the tree in bottom up fashion.
        In case it's sorted array, part arrays could be sent to balanced_bst
        recursive function to create the tree, still in bottom up fashion
        """
        nonlocal index

        if n <= 0:
            return None

        left_nodes = int(n / 2)
        left = balanced_bst(left_nodes)
        node = Node(ll[index])
        node.left = left
        index += 1
        node.right = balanced_bst(n - left_nodes - 1)
        return node

    l: int = len(ll)
    index: int = 0
    return balanced_bst(l)


if __name__ == "__main__":
    ll = [1, 2, 3, 4, 5, 6, 7]
    print(inorder(create_balanced_bst(ll)))
