"""
Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""


class Node:
    def __init__(self, val: str, left=None, right=None):
        # space characters are not allowed as value
        self.val = val
        self.left = left
        self.right = right


# serialize using in-order traversal
def serialize(root):
    if not root:
        return "None"

    return f"{str(root.val)} {serialize(root.left)} {serialize(root.right)}"
