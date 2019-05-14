class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class LinkedList:
    def __init__(self, head: Node = None):
        self.head = head

    def push(self, data: int):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            h = self.head

            while h.next:
                h = h.next

            h.next = node

        return self

    def __len__(self):
        head: Node = self.head
        count: int = 0

        while head:
            count += 1
            head = head.next

        return count
