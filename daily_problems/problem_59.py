"""
Implement a file syncing algorithm for two computers over a low-bandwidth network.
What if we know the files in the two computers are mostly the same?
"""
from itertools import zip_longest
from typing import Optional
from hashlib import md5


class MerkleTree:
    """
    Merke tree: A tree in which every leaf node is labelled with
    the hash of a data block, and every non-leaf node is labelled
    with the cryptographic hash of the labels of its child nodes
    """

    def __init__(self, is_dir: bool = False) -> None:
        self.data: str = ""
        self.hash: str = ""
        self.children: list = []
        self.is_dir: bool = is_dir
        self.parent: Optional[MerkleTree] = None

    def __repr__(self) -> str:
        return f"{self.data} - {self.hash}"

    def set_content(self, content: str) -> None:
        if self.is_dir:
            raise AssertionError("Invalid")

        self.data = content
        self.recalculate_directory_hash()

    def add_to_directory(self, directory) -> None:
        directory.children.append(self)
        self.parent = directory
        self.recalculate_directory_hash()

    def recalculate_directory_hash(self) -> None:
        parent = self.parent

        if not self.is_dir:
            self.hash = md5(self.data.encode()).hexdigest()

        while parent:
            children = parent.children
            collated_hash = ""
            for child in children:
                collated_hash += child.hash

            parent.hash = md5(collated_hash.encode()).hexdigest()
            parent = parent.parent


def get_files_that_are_different(
    root_1: MerkleTree, root_2: MerkleTree, change_1: list, change_2: list
):
    if not (root_1 or root_2):
        return change_1, change_2
    if not (root_1 and root_2):
        change_1.append(root_2)
        change_2.append(root_1)
        return change_1, change_2
    if root_1.hash != root_2.hash:
        change_1.append(root_2)
        change_2.append(root_1)

        for c1, c2 in zip_longest(root_1.children, root_2.children):
            get_files_that_are_different(c1, c2, change_1, change_2)

    return change_1, change_2


if __name__ == "__main__":
    # create a directory structure on the first computer
    root_directory = MerkleTree(True)

    file1 = MerkleTree()
    file1.add_to_directory(root_directory)
    file1.set_content("owl city rocks!")

    file2 = MerkleTree()
    file2.add_to_directory(root_directory)
    file2.set_content("owl city rocks again!")

    directory_2 = MerkleTree(True)
    directory_2.add_to_directory(root_directory)

    file3 = MerkleTree()
    file3.add_to_directory(directory_2)
    file3.set_content("owl city rocks!")

    # create a directory structure on the second computer
    root_directory_2 = MerkleTree(True)

    file1_2 = MerkleTree()
    file1_2.add_to_directory(root_directory_2)
    file1_2.set_content("owl city rocks!")

    file2_2 = MerkleTree()
    file2_2.add_to_directory(root_directory_2)
    file2_2.set_content("owl city rocks again!")

    directory_2_2 = MerkleTree(True)
    directory_2_2.add_to_directory(root_directory_2)

    file3_2 = MerkleTree()
    file3_2.add_to_directory(directory_2_2)
    file3_2.set_content("owl city rocks! pop")

    file_changes_for_system_1, file_changes_for_system_2 = get_files_that_are_different(
        root_directory, root_directory_2, [], []
    )

    print(file_changes_for_system_1)
    print(file_changes_for_system_2)
