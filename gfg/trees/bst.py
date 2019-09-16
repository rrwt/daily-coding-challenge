"""
Insert, search and Delete in a BST
"""
from typing import Optional, Tuple

from tree_traversal import inorder  # type: ignore


class BST:
    """Binary Search Tree.
    An implementation of BST search, insert and delete
    """

    def __init__(self) -> None:
        self.root: Optional[Node] = None  # type: ignore

    class Node:
        def __init__(self, data: int) -> None:
            self.data = data
            self.left: Optional[None] = None
            self.right: Optional[None] = None

    def insert(self, value_to_insert: int) -> None:
        """Insert a new node to the BST
        
        Time Complexity: O(log(h)), where h is height of the tree
        Space Complexity: O(1)

        :param value_to_insert: Value to be inserted to BST
        :type value_to_insert: int
        :raises AssertionError: In case of duplicated data
        :return: None
        """
        node = BST.Node(value_to_insert)

        if self.root is None:
            self.root = node
        else:
            runner = self.root

            while runner:
                if value_to_insert == runner.data:
                    raise AssertionError("Duplicate Data")
                elif value_to_insert < runner.data:
                    if runner.left:
                        runner = runner.left
                    else:
                        runner.left = node
                        break
                else:
                    if runner.right:
                        runner = runner.right
                    else:
                        runner.right = node
                        break

    def search(self, value_to_search: int) -> Tuple[Optional[Node], bool]:
        """Search for a value in BST
        
        Time Complexity: O(log(h)), where h is height of the tree
        Space Complexity: O(1)

        :param value_to_search: Value being searched for
        :type value_to_search: int
        :return: tuple
        """
        runner = self.root

        while runner:
            if runner.data == value_to_search:
                return runner, True
            elif value_to_search < runner.data:
                runner = runner.left
            else:
                runner = runner.right

        return None, False

    def delete(self, value_to_delete: int) -> bool:
        """Delete a value from BST

        Following Cases Arise:
            1. Does Not Exist: We return none
            2. Is at the leaf: Delete and return the value
            3. Is not a leaf:
                a. Has both children: Replace the value with inorder successor
                                      and delete the successor
                b. Only one child: Replace value with child's value and delete child recursively
        
        Time Complexity: O(n), where n is number of nodes in the tree
        Space Complexity: O(1)

        :param value_to_delete: value to be deleted
        :type value_to_delete: int
        :return: True|False
        :rtype: bool
        """

        def min_value_key(node):
            if node is None:
                return None

            while node and node.left:
                node = node.left

            return node

        def delete_node(root):
            if root is None:
                return root

            if root.data == value_to_delete:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None and root.right is not None:
                    root.data, root.right.data = root.right.data, root.data
                    root.right = delete_node(root.right)
                elif root.right is None and root.left is not None:
                    root.data, root.left.data = root.left.data, root.data
                    root.left = delete_node(root.left)
                else:
                    successor = min_value_key(root.right)
                    root.data, successor.data = successor.data, root.data
                    root.right = delete_node(root.right)
            if root.data > value_to_delete:
                root.left = delete_node(root.left)
            else:
                root.right = delete_node(root.right)

            return root

        if self.root is not None:
            self.root = delete_node(self.root)
            return True

        return False


if __name__ == "__main__":
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder Traversal")
    inorder(bst.root)
    print()

    print("Delete 20")
    bst.delete(20)
    print("Inorder traversal of the modified tree")
    inorder(bst.root)
    print()

    print("Searching")
    print(bst.search(20))
    print(bst.search(30))

    print("Delete 30")
    bst.delete(30)
    print("Inorder traversal of the modified tree")
    inorder(bst.root)
    print()

    print("Delete 50")
    bst.delete(50)
    print("Inorder traversal of the modified tree")
    inorder(bst.root)
    print()
