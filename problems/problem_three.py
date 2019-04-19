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
def serialize(root: Node) -> str:
    if not root:
        return "None"

    return f"{str(root.val)} {serialize(root.left)} {serialize(root.right)}"


def deserialize(string: str) -> Node:
    ptr = 0

    def deserializer(str_arr: list):
        nonlocal ptr
        root = Node(str_arr[ptr]) if str_arr[ptr] != "None" else None

        if root:
            ptr += 1
            root.left = deserializer(str_arr)
            ptr += 1
            root.right = deserializer(str_arr)

        return root

    return deserializer(string.split(" "))
