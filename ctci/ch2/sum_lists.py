"""
You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1 's digit
is at the head of the list. Write a function that adds the two numbers and
returns the sum as a linked list.

EXAMPLE
Input:(7-> 1 -> 6) + (5 -> 9 -> 2) i.e. 617 + 295.
Output:2 -> 1 -> 9. i.e. 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5). That is,617 + 295.
Output:9 -> 1 -> 2. That is, 912.
"""
from list_structure import Node, LinkedList


def sum_reverse(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    time complexity: O(m+n), where m and n are respective lengths of given strings
    space complexity: O(m+n)
    """
    head1: Node = ll1.head
    head2: Node = ll2.head
    result: LinkedList = LinkedList()
    data: int = 0
    carry: int = 0

    while head1 and head2:
        data = head1.data + head2.data + carry
        data, carry = data % 10, int(data/10)
        result.push(data)
        head1 = head1.next
        head2 = head2.next

    while head1:
        data = head1.data + carry
        data, carry = data % 10, int(data/10)
        result.push(data)
        head1 = head1.next

    while head2:
        data = head2.data + carry
        data, carry = data % 10, int(data/10)
        result.push(data)
        head2 = head2.next

    if carry:
        result.push(carry)

    return result


def sum_forward(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Recursive solution would work here better as we need to traverse the singly list in reverse.
    We can pad the smaller list to get accurate result
    """
    def get_recursive_sum(h1: Node, h2: Node, carry: int = 0):
        if not h1:
            return None, 0

        h2next, h2data = (h2.next, h2.data) if h2 else (None, 0)

        returned_node, carry = get_recursive_sum(h1.next, h2next, 0)

        data: int = h1.data + h2data + carry
        data, carry = data % 10, int(data/10)
        node = Node(data)
        node.next = returned_node
        return node, carry

    head1: Node = ll1.head
    head2: Node = ll2.head
    result: LinkedList = LinkedList()
    l1 = len(ll1)
    l2 = len(ll2)

    diff: int = l1-l2

    if diff:
        if diff > 0:
            for _ in range(diff):
                node = Node(0)
                node.next = head2
                head2 = node
        else:
            for _ in range(abs(diff)):
                node = Node(0)
                node.next = head1
                head1 = node

    head, carry = get_recursive_sum(head1, head2)

    if carry:
        result.head = carry
        carry.next = head
    else:
        result: LinkedList = LinkedList()
        result.head = head

    return result


if __name__ == "__main__":
    ll1 = LinkedList(Node(7))  # 7-1-6
    ll1.push(1).push(6)

    ll2 = LinkedList(Node(5))  # 5-9-2-1
    ll2.push(9).push(2).push(1)

    result: LinkedList = sum_reverse(ll1, ll2)  # 2-1-9-1
    h: Node = result.head

    while h.next:
        print(h.data, end='->')
        h = h.next
    print(h.data)

    result = sum_forward(ll1, ll2)  # 6-6-3-7
    h: Node = result.head

    while h.next:
        print(h.data, end='->')
        h = h.next
    print(h.data)
