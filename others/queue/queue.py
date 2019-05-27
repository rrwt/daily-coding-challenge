"""
Implementation of queue, deque, circular queue and priority queue
"""
from typing import Union, Optional
import math


class Node:
    """
    A queue node with data and next pointer
    """

    def __init__(self, data: Union[int, str]):
        self.data = data
        self.next: Optional[Node] = None


class DNode:
    """
    A deque node with data and next and previous pointer
    """

    def __init__(self, data: Union[int, str]):
        self.data = data
        self.next: Optional[DNode] = None
        self.previous: Optional[DNode] = None


class PNode:
    """
    A Priority queue node with data, next pointer and priority
    """

    def __init__(self, data: Union[int, str], priority: int):
        self.data = data
        self.next: Optional[PNode] = None
        self.priority = priority


class Queue:
    def __init__(self, size: Optional[int]):
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None
        self.size: int = size or int(math.pow(2, 64))
        self.count = 0

    def is_full(self):
        return self.count >= self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data: Union[int, str]):
        if self.is_full():
            raise Exception("Queue Overflow")

        node = Node(data)

        if self.is_empty():
            self.front = node
        elif self.rear:
            self.rear.next = node

        self.rear = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")

        node = self.front
        self.front = self.front.next

        if self.count == 1:
            self.rear = None

        self.count -= 1
        return node


class CircularQueue(Queue):
    """
    A queue with the next of last pointer pointing to the first one
    """

    def enqueue(self, data: Union[int, str]):
        super().enqueue(data)
        if self.rear:
            self.rear.next = self.front

    def dequeue(self):
        node = super().dequeue()

        if self.count():
            self.rear.next = self.front

        return node


class PriorityQueue:
    """
    Cannot be a subclass of queue: It violates liskoff substitution principle
    """

    def __init__(self, size: Optional[int]):
        self.front: Optional[PNode] = None
        self.rear: Optional[PNode] = None
        self.size: int = size or int(math.pow(2, 64))
        self.count = 0

    def is_full(self):
        return self.count >= self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data: Union[int, str], priority: int):
        if self.is_full():
            raise Exception("Queue Overflow")

        node = PNode(data, priority)

        if self.is_empty():
            self.front = self.rear = node
        elif self.front:
            if node.priority > self.front.priority:
                node.next = self.front
                self.front = node
            else:
                head = self.front

                while head.next and head.next.priority > node.priority:
                    head = head.next

                head.next, node.next = node, head.next

        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")

        node = self.front
        self.front = self.front.next

        if self.count == 1:
            self.rear = None

        self.count -= 1
        return node


class Deque:
    """
    Double ended queue with both previous and next pointers
    """

    def __init__(self, size: Optional[int]):
        self.front: Optional[DNode] = None
        self.rear: Optional[DNode] = None
        self.size: int = size or int(math.pow(2, 64))
        self.count = 0

    def is_full(self):
        return self.count >= self.size

    def is_empty(self):
        return self.count == 0

    def enqueue(self, data: Union[int, str]):
        if self.is_full():
            raise Exception("Queue Overflow")

        node = DNode(data)

        if self.is_empty():
            self.front = node
        elif self.rear:
            self.rear.next = node
            node.previous = self.rear

        self.rear = node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue Underflow")

        node = self.front
        self.front = self.front.next

        if self.count == 1:
            self.rear = None

        self.count -= 1
        return node
