"""
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest"
(based on arrival time) of all animals at the shelter, or they can select whether
they would prefer a dog or a cat (and will receive the oldest animal of that type).
They cannot select which specific animal they would like. Create the data structures
to maintain this system and implement operations such as enqueue, dequeueAny,
dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.
"""
from __future__ import annotations
from typing import Optional
from enum import Enum
from collections import deque


class AnimalKind(Enum):
    cat = "cat"
    dog = "dog"


class Animal:
    def __init__(self, name: str, order: int):
        self.name = name
        self.order = order

    def is_older(self, other: Animal) -> bool:
        return self.order < other.order


class AnimalShelterQueue:
    def __init__(self):
        self.dog = deque()
        self.cat = deque()
        self.order: int = 0

    def enqueue(self, name: str, kind: AnimalKind):
        node = Animal(name, self.order)
        self.order += 1

        if kind == AnimalKind.cat:
            self.cat.append(node)
        elif kind == AnimalKind.dog:
            self.dog.append(node)
        else:
            raise ValueError(kind)

    def dequeueAny(self) -> Optional[Animal]:
        if self.dog and self.cat:
            if self.dog[0].is_older(self.cat[0]):
                return self.dog.popleft()
            else:
                return self.cat.popleft()
        elif self.dog:
            return self.dog.popleft()
        elif self.cat:
            return self.cat.popleft()

        return None

    def dequeueCat(self) -> Optional[Animal]:
        return self.cat.popleft() if self.cat else None

    def dequeueDog(self) -> Optional[Animal]:
        return self.dog.popleft() if self.dog else None


if __name__ == "__main__":
    animals = AnimalShelterQueue()
    animals.enqueue("perro", AnimalKind.dog)
    animals.enqueue("gato", AnimalKind.cat)

    first = animals.dequeueAny()
    second = animals.dequeueCat()

    assert first is not None and first.name == "perro"
    assert animals.dequeueDog() is None
    assert second is not None and second.name == "gato"
