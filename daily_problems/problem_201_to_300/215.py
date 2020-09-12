"""
The horizontal distance of a binary tree node describes
how far left or right the node will be when the tree is printed out.
More rigorously, we can define it as follows:
    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.
For example, for the following tree, hd(1) = -2, and hd(6) = 0.
             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance.
If there are two nodes at the same depth and horizontal distance, either is acceptable.
For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].
Given the root to a binary tree, return its bottom view.
"""
from typing import Optional, List, Dict

from daily_problems.binary_tree_node import Node


def _bottom_view(
    root_node: Optional[Node], view: dict, position: int
) -> Dict[int, int]:
    if not root_node:
        return view

    view[
        position
    ] = root_node.data  # always override, bottommost view is more important
    view = _bottom_view(root_node.left, view, position - 1)
    view = _bottom_view(root_node.right, view, position + 1)
    return view


def bottom_view(root_node: Node) -> List[int]:
    view = _bottom_view(root_node, {}, 0)
    start_index = min(view.keys())
    end_index = max(view.keys())

    return [view[index] for index in range(start_index, end_index + 1)]


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(4)
    root.left.left.left = Node(0)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(9)
    root.right.right.left = Node(8)
    print(bottom_view(root))
