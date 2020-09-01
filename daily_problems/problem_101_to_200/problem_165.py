"""
Given an array of integers, return a new array where each element in the new array
is the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
    There is 1 smaller element to the right of 3
    There is 1 smaller element to the right of 4
    There are 2 smaller elements to the right of 9
    There is 1 smaller element to the right of 6
    There are no smaller elements to the right of 1
"""
from typing import List


def num_smaller_to_right_naive(nums: List[int]) -> List[int]:
    length = len(nums)
    return_list = [0] * length

    for i, el in enumerate(nums):
        for j in range(i + 1, length):
            if nums[j] < el:
                return_list[i] += 1

    return return_list


class BSTNode:
    def __init__(self, data: int, l_count: int = 0) -> None:
        self.left = self.right = None
        self.data = data
        self.l_count = l_count


class BST:
    def __init__(self, root: int) -> None:
        self.root = BSTNode(root)

    def insert(self, data: int) -> int:
        root = self.root
        cur_count = 0

        while root:
            if root.data > data:
                root.l_count += 1
                if root.left:
                    root = root.left
                else:
                    root.left = BSTNode(data, cur_count)
                    break
            elif root.data < data:
                cur_count += root.l_count + 1
                if root.right:
                    root = root.right
                else:
                    root.right = BSTNode(data)
                    break

        return cur_count


def num_smaller_to_right_bst(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(n * log(n))
    Space Complexity: O(n)
    """
    bst = BST(nums[-1])
    length = len(nums)
    count_arr = [0] * length

    for index in range(length - 2, -1, -1):
        count_arr[index] = bst.insert(nums[index])

    return count_arr


if __name__ == "__main__":
    assert num_smaller_to_right_naive([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
    assert num_smaller_to_right_bst([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
    assert num_smaller_to_right_bst([10, 6, 15, 20, 30, 5, 7]) == [3, 1, 2, 2, 2, 0, 0]
