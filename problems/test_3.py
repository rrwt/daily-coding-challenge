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

from .problem_3 import Node, serialize, deserialize


class TestSerializeDeserializeTree:
    def test_can_create_tree(self):
        node = Node('root')
        assert node.val == 'root'
        assert node.left is None
        assert node.right is None

    def test_can_attach_right_and_left_children_to_tree(self):
        left = Node('left')
        right = Node('right')
        root = Node('root', left, right)

        assert root.val == 'root'
        assert root.left.val == 'left'
        assert root.right.val == 'right'

    def test_can_serialize_tree_with_only_root_element(self):
        root = Node('root')
        assert serialize(root) == "root None None"

    def test_can_serialize_tree_with_children(self):
        root = Node('root', Node('left'), Node('right'))
        assert serialize(root) == "root left None None right None None"

        root = Node('root', Node('left', Node('left.left')), Node('right'))
        assert serialize(root) == "root left left.left None None None right None None"

    def test_can_deserialize_a_serialized_node(self):
        root = Node('root')

        serialized_str = serialize(root)
        deserialized_tree = deserialize(serialized_str)

        assert serialized_str == "root None None"
        assert deserialized_tree.val == root.val
        assert deserialized_tree.left == root.left
        assert deserialized_tree.right == root.right

    def test_can_deserialize_a_serialized_binary_tree(self):
        node = Node("root", Node("left", Node("left.left")), Node("right"))
        assert deserialize(serialize(node)).left.left.val == "left.left"
