"""
Find an efficient algorithm to find the smallest distance (measured in number of words)
between any two given words in a string.

For example,
    given words "hello", and "world" and a text content of
    "dog cat hello cat dog dog hello cat world",
    return 1 because there's only one word "cat" in between the two words.
"""
from collections import defaultdict


def shortest_distance(text: str, first: str, second: str) -> int:
    d = defaultdict(int)
    min_dist = len(text)

    for index, word in enumerate(text.split(" ")):
        if word == first:
            d[word] = index

            if second in d:
                min_dist = min(abs(d[second] - d[first] - 1), min_dist)
        elif word == second:
            d[word] = index
            if first in d:
                min_dist = min(abs(d[second] - d[first] - 1), min_dist)

    return min_dist


if __name__ == "__main__":
    assert (
        shortest_distance("dog cat hello cat dog dog hello cat world", "hello", "world")
        == 1
    )
