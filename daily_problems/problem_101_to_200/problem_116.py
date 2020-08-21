"""
Generate a finite, but an arbitrarily large binary tree quickly in O(1).
That is, generate() should return a tree whose size is unbounded but finite.
"""
import random


class Node1:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_1():
    """
    Eager tree generation
    If we ignore the O(1) generation constraint,
    we can create an unbounded tree by using randomness.
    That is, we can generate the left and right sub-trees recursively X% of the time.
    Since the question does not have any constraints about the values the nodes can have,
    we’ll arbitrarily set it to 0.
    """
    root = Node1(0)

    if random.random() > 0.5:
        root.left = generate_1()
    if random.random() > 0.5:
        root.right = generate_1()

    return root


class Node2:
    """
    Lazy tree generation
    The trick here is that we can generate the tree lazily. Here we use Python’s property keyword,
    which lets us define a property on an object at look-up.
    When the left or right property is looked up, we check if that sub-tree has been evaluated.
    If not, we recursively create a new node half the time. If it has been evaluated already,
    then we just return that node.
    The object is created in constant time since none of the subtrees
    are evaluated when it’s created.
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False

    @property
    def left(self):
        if not self._is_left_evaluated:
            if random.random() > 0.5:
                self._left = Node2(0)

        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            if random.random() > 0.5:
                self._right = Node2(0)

        self._is_right_evaluated = True
        return self._right


def generate_2():
    return Node2(0)
