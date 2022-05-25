"""
Implement a function to check if a linked list is a palindrome.
"""
from list_structure import Node, LinkedList


def palindrome(ll: LinkedList) -> bool:
    """
    We can recursively call the list, and it's reverse and check if they match
    """

    def palindrome_recursive(t: Node) -> bool:
        nonlocal head

        if not t:
            return True

        p: bool = palindrome_recursive(t.next)

        if p and head.data == t.data:
            head = head.next
            return True

        return False

    head: Node = ll.head
    tail: Node = ll.head

    return palindrome_recursive(tail)


if __name__ == "__main__":
    ll = LinkedList(Node(1))
    ll.push(2).push(3).push(4).push(3).push(2).push(1)

    assert palindrome(ll) == True
