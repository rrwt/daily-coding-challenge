"""
Write a function that checks whether a given Linked List contains loop and
if loop is present then removes the loop and returns true.
If the list doesn’t contain loop then it returns false.
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def detect_and_remove_loop(ll: Node) -> bool:
    if ll:
        fast: Node = ll
        slow: Node = ll

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break
        if fast and fast.next:
            slow = ll

            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

            fast.next = None
            return True

    return False


if __name__ == "__main__":
    ll: Node = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)
    ll.next.next.next.next.next = ll.next

    print(detect_and_remove_loop(ll))
