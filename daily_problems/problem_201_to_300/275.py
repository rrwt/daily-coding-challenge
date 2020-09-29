"""
The "look and say" sequence is defined as follows:
beginning with the term 1, each subsequent term visually describes the
digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.
Given an integer N, print the Nth term of this sequence.
"""
from functools import lru_cache
from typing import List


@lru_cache(maxsize=32)
def look_and_say(n: int) -> List[int]:
    if n == 1:
        return [1]

    prev = look_and_say(n - 1)
    index = 0
    size = len(prev)
    res = []

    while index < size:
        val = prev[index]
        count = 0

        while index < size and val == prev[index]:
            count += 1
            index += 1

        res.append(count)
        res.append(val)

    return res


if __name__ == "__main__":
    assert look_and_say(1) == [1]
    assert look_and_say(2) == [1, 1]
    assert look_and_say(3) == [2, 1]
    assert look_and_say(4) == [1, 2, 1, 1]
    assert look_and_say(5) == [1, 1, 1, 2, 2, 1]
    assert look_and_say(6) == [3, 1, 2, 2, 1, 1]
    assert look_and_say(7) == [1, 3, 1, 1, 2, 2, 2, 1]
