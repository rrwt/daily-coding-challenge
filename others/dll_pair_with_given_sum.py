"""
Given a sorted DLL, find a pair of elements with given sum x
"""


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class DLL:
    def __init__(self, head=None):
        self.head = head

    def get_tail(self):
        t = self.head

        while t.next:
            t = t.next

        return t

    # O(n)
    def find(self, x):
        h = self.head
        t = self.get_tail()

        while h != t:
            sum_ = h.data + t.data

            if sum_ == x:
                print(f"The elements with sum {x} are: {h.data} and {t.data}")
                return

            if sum_ < x:
                h = h.next
            else:
                t = t.prev


if __name__ == "__main__":
    dll = DLL(Node(1))
    two = dll.head.next = Node(2, dll.head)
    three = two.next = Node(3, two)
    six = three.next = Node(6, three)
    six.next = Node(10, six)

    print("DLL", end=": ")

    t = dll.head

    while t.next:
        print(t.data, end=" ")
        t = t.next

    print(t.data)

    dll.find(9)
