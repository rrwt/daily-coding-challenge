"""
You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.
For example,
    given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
    you should return ['x', 'z', 'w', 'y'].
"""
from typing import List


def get_characters(dictionary: List[str]) -> set:
    s = set()

    for word in dictionary:
        for char in word:
            s.add(char)

    return s


def dfs(graph: dict, src: str, visited: set, pool: List) -> List[str]:
    visited.add(src)

    for dst in graph[src]:
        if dst not in visited:
            pool = dfs(graph, dst, visited, pool)

    pool.append(src)
    return pool


def topological_sorting(graph: dict) -> List[str]:
    visited = set()
    pool = []

    for src in graph.keys():
        if src not in visited:
            pool = dfs(graph, src, visited, pool)

    return pool[::-1]


def order_of_letters(dictionary: List[str]) -> List[str]:
    characters = get_characters(dictionary)
    index = 0
    size = len(dictionary)

    hash_map = {}

    for char in characters:
        hash_map[char] = []

    while index < size - 1:
        for c1, c2 in zip(dictionary[index], dictionary[index + 1]):
            if c1 != c2:
                hash_map[c1].append(c2)
                break

        index += 1

    # topological sort
    return topological_sorting(hash_map)


if __name__ == "__main__":
    assert order_of_letters(["xww", "wxyz", "wxyw", "ywx", "ywz"]) == ["x", "z", "w", "y"]
    assert order_of_letters(["baa", "abcd", "abca", "cab", "cad"]) == ["b", "d", "a", "c"]
