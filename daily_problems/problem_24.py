"""
Implement locking in a binary tree. A binary tree node can be locked
or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:
    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should
          return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return
          false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like.
You may assume the class is used in a single-threaded program,
so there is no need for actual locks or mutexes. Each method should run in O(h),
where h is the height of the tree.
"""
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None
        self.locked: bool = False
        self.locked_desc: int = 0

    def __repr__(self):
        return f"{self.data} - {self.locked}"


class LockingBinaryTree:
    """
    Can be solved using 2 different methods with different costs of operation
    1. Time complexity: O(h) - lock/unlock and O(1) - check if locked
       Keep count of how many child nodes of current node are locked and use it to
       find out if the locking condition based on child nodes. Parent node locking
       condition can be looked for by climbing up the tree.
    2. Time complexity: O(1) - check if locked/unlock. O(h+m) - lock. m = number of children
       check and unlock in O(1). While locking check if there is any locked parent O(h) node
       or locked child O(m) node.
    """

    def __init__(self, root: Node = None):
        self.root = root

    def _is_subtree_locked(self, node: Optional[Node] = None) -> bool:
        if node is None:
            return False

        if node.locked or node.locked_desc > 0:
            return True

        return self._is_subtree_locked(node.left) or self._is_subtree_locked(node.right)

    def _is_parent_tree_locked(self, node: Optional[Node] = None) -> bool:
        if not node:
            return False

        return node.locked or self._is_parent_tree_locked(node.parent)

    def incr_parent_lock_count(self, node: Optional[Node] = None) -> None:
        while node:
            node.locked_desc += 1
            node = node.parent

    def decr_parent_lock_count(self, node: Optional[Node] = None) -> None:
        while node:
            if node.locked_desc > 0:
                node.locked_desc -= 1
                node = node.parent
            else:
                break

    def lock(self, node: Optional[Node] = None) -> bool:
        """
        Lock a node if possible
        Time Complexity: O(h)
        """
        if node:
            if self._is_parent_tree_locked(node) or self._is_subtree_locked(node):
                return False

            node.locked = True
            self.incr_parent_lock_count(node.parent)
            return True

        return False

    def unlock(self, node: Optional[Node] = None) -> bool:
        """
        UnLock a node if possible
        Time Complexity: O(h)
        """
        if node and node.locked:
            node.locked = False
            self.decr_parent_lock_count(node.parent)
            return True

        return False

    def is_locked(self, node: Optional[Node] = None) -> bool:
        """
        Check if the node is locked
        Time complexity: O(1)
        """
        if node:
            return node.locked
        return False


if __name__ == "__main__":
    lbt = LockingBinaryTree()
    root = lbt.root = Node(1)
    root.left = Node(2)
    root.left.parent = root
    root.right = Node(3)
    root.right.parent = root

    assert lbt.lock(root.left)
    assert lbt.lock(root) is False
    assert lbt.lock(root.right)
    assert lbt.unlock(root.left)
    assert lbt.unlock(root) is False
    assert lbt.unlock(root.right)
    assert lbt.lock(root)
    assert lbt.lock(root.left) is False
    assert lbt.lock(root.right) is False
