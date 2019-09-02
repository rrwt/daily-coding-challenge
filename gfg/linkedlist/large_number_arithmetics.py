"""
Large number arithmetic using doubly linked list
Given two very large numbers in form of strings.
Your task is to apply different arithmetic operations on these strings.
"""
from typing import Optional


class Node:
    def __init__(self, data: int):
        self.data = data
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LargeNumberArithmetics:
    def __init__(self, first_number: str, second_number: str):
        self.first = self._string_to_dll(first_number)
        self.second = self._string_to_dll(second_number)
        self.result = {}

    @staticmethod
    def _string_to_dll(string_number) -> dict:
        head = None
        tail = None

        for char in string_number:
            try:
                value = int(char)
            except ValueError:
                raise AssertionError("invalid integer")

            if head is None:
                head = Node(value)
                tail = head
            else:
                tail.next = Node(value)
                tail.next.prev = tail
                tail = tail.next

        return {"head": head, "tail": tail}

    def prepend_to_result(self, node: Optional[Node]) -> None:
        if node:
            if "head" in self.result:
                node.right = self.result["head"]
                self.result["head"].left = node
                self.result["head"] = node
            else:
                self.result["head"] = self.result["tail"] = node

    def add(self) -> None:
        tail1 = self.first["tail"]
        tail2 = self.second["tail"]
        carry = 0

        while tail1 and tail2:
            digit_sum, carry = divmod(tail1.data + tail2.data + carry, 10)
            self.prepend_to_result(Node(digit_sum))
            tail1 = tail1.prev
            tail2 = tail2.prev

        while tail1:
            digit_sum, carry = divmod(tail1.data + carry, 10)
            self.prepend_to_result(Node(digit_sum))
            tail1 = tail1.left

        while tail2:
            digit_sum, carry = divmod(tail2.data + carry, 10)
            self.prepend_to_result(Node(digit_sum))
            tail2 = tail2.left

        if carry:
            self.prepend_to_result(Node(carry))

    def subtract(self) -> None:
        tail1 = self.first["tail"]
        tail2 = self.second["tail"]
        carry = 0

        while tail1 and tail2:
            diff = tail1.data - tail2.data + carry

            if diff < 0:
                diff = -diff
                carry = -1

            self.prepend_to_result(Node(diff))
            tail1 = tail1.prev
            tail2 = tail2.prev

        while tail1:
            diff = tail1.data - tail2.data + carry

            if diff < 0:
                diff = -diff
                carry = -1

            self.prepend_to_result(Node(diff))
            tail1 = tail1.left

        while tail2:
            diff = tail1.data - tail2.data + carry

            if diff < 0:
                diff = -diff
                carry = -1

            self.prepend_to_result(Node(diff))
            tail2 = tail2.left

        if carry:
            self.result["head"].data = -self.result["head"].data


if __name__ == "__main__":
    pass
