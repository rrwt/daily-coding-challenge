"""
How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node = None
        self.prev: Node = None


class Stack:
    def __init__(self):
        self.head = None
        self.middle = None
        self.node_count: int = 0

    def push(self, value: int):
        node = Node(value)
        self.node_count += 1

        if self.head:
            self.head.prev = node
            node.next = self.head

            if self.node_count & 1:
                self.middle = self.middle.prev
        else:
            self.middle = node

        self.head = node

    def pop(self) -> int:
        if not self.head:
            raise Exception("Stack underflow")

        value = self.head.data
        next_node = self.head.next

        if next_node:
            next_node.prev = None
            del self.head

        self.head = next_node
        self.node_count -= 1

        if self.node_count & 1 == 0:
            if self.node_count:
                self.middle = self.middle.next
            else:
                self.middle = self.head

        return value

    def find_middle(self) -> int:
        if not self.middle:
            raise Exception("Stack underflow")
        return self.middle.data

    def delete_middle(self):
        if not self.middle:
            raise Exception("Stack underflow")
        if self.node_count < 3:
            self.head = self.head.next
            self.middle = self.head
            self.node_count -= 1
        else:
            prev = self.middle.prev
            prev.next = self.middle.next
            self.middle.next.prev = prev
            self.node_count -= 1
            self.middle = self.middle.next


if __name__ == "__main__":
    ms = Stack()
    ms.push(11)
    ms.push(22)
    ms.push(33)
    ms.push(44)
    ms.push(55)
    ms.push(66)
    ms.push(77)

    print(ms.pop())
    print(ms.pop())
    print(ms.find_middle())
    ms.delete_middle()
    print(ms.find_middle())
