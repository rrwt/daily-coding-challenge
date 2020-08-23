"""
Let's represent an integer in a linked list format by having each node represent
a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:
    1 -> 2 -> 3 -> 4 -> 5 is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.
For example, given
    9 -> 9
    5 -> 2
    return 124 (99 + 25) as:

    4 -> 2 -> 1
"""
from daily_problems.linked_list import Node


def sum_ll(head_1: Node, head_2: Node) -> Node:
    head = tail = None
    carry = 0

    while head_1 and head_2:
        cur_sum = head_1.data + head_2.data + carry
        cur_sum, carry = cur_sum % 10, cur_sum // 10

        if not head:
            head = tail = Node(cur_sum)
        else:
            tail.next = Node(cur_sum)
            tail = tail.next

        head_1 = head_1.next
        head_2 = head_2.next

    while head_1:
        cur_sum = head_1.data + carry
        cur_sum, carry = cur_sum % 10, cur_sum // 10
        tail.next = Node(cur_sum)
        tail = tail.next
        head_1 = head_1.next

    while head_2:
        cur_sum = head_2.data + carry
        cur_sum, carry = cur_sum % 10, cur_sum // 10
        tail.next = Node(cur_sum)
        tail = tail.next
        head_2 = head_2.next

    if carry:
        tail.next = Node(carry)

    return head


if __name__ == "__main__":
    root_1 = Node(9)
    root_1.next = Node(9)
    root_2 = Node(5)
    root_2.next = Node(2)

    root = sum_ll(root_1, root_2)

    while root:
        print(root.data)
        root = root.next
