"""
Efficiently implement k Queues in a single array
"""
from array import array
from random import randint


class Queues:
    def __init__(self, size: int, noq: int):
        if size < noq:
            raise Exception("Size of the array cannot be smaller than number of queues")

        self.array = array("b", [-1] * size)
        self.size = size
        self.noq = noq
        self.next_free_slot: int = 0
        self.next_element = array("b", (_ + 1 for _ in range(size)))
        self.next_element[-1] = -1
        self.front = array("b", [-1] * noq)
        self.rear = array("b", [-1] * noq)

    def is_full(self):
        return self.next_free_slot == -1

    def is_empty(self, queue):
        return self.front[queue] == -1

    def enqueue(self, element: int, queue: int):
        if self.is_full():
            raise Exception("Queue overflow")
        if queue >= self.noq:
            raise Exception("Invalid queue number")

        curr_free_pos = self.next_free_slot
        self.next_free_slot = self.next_element[curr_free_pos]

        if self.is_empty(queue):
            self.front[queue] = curr_free_pos
        else:
            self.next_element[self.rear[queue]] = curr_free_pos

        self.rear[queue] = curr_free_pos
        self.next_element[curr_free_pos] = -1  # last element of queue
        self.array[curr_free_pos] = element

    def dequeue(self, queue: int):
        if self.is_empty(queue):
            raise Exception("Queue Underflow")

        if queue >= self.noq:
            raise Exception("Invalid queue Number")

        curr_pos = self.front[queue]
        data = self.array[curr_pos]
        self.array[curr_pos] = -1
        self.front[queue] = self.next_element[curr_pos]

        if self.front[queue] == -1:
            self.rear[queue] = -1

        self.next_element[curr_pos] = self.next_free_slot
        self.next_free_slot = curr_pos
        return data


if __name__ == "__main__":
    noq = 3
    q = Queues(10, noq)

    for _ in range(10):
        q.enqueue(_, randint(0, noq - 1))

    print("->".join(map(str, q.array)))
    print("->".join(map(str, q.front)))
    print("->".join(map(str, q.rear)))
    print("->".join(map(str, q.next_element)))

    print("dequeued item from 0th queue is", q.dequeue(0), sep=" ")
    print("dequeued item from 1st queue is", q.dequeue(1), sep=" ")
    print("dequeued item from 2nd queue is", q.dequeue(2), sep=" ")
    print("->".join(map(str, q.array)))
    print("->".join(map(str, q.front)))
    print("->".join(map(str, q.rear)))
    print("->".join(map(str, q.next_element)))

    for _ in range(3):
        q.enqueue(randint(1, 100), randint(0, noq - 1))

    print("->".join(map(str, q.array)))
    print("->".join(map(str, q.front)))
    print("->".join(map(str, q.rear)))
    print("->".join(map(str, q.next_element)))

    for i in range(3):
        print("printing queue", i, sep=" ")

        head = q.front[i]

        while head > -1 and head != q.rear[i]:
            print(q.array[head], end="->")
            head = q.next_element[head]

        print(q.array[head])
