"""
A classroom consists of N students, whose friendships can be
represented in an adjacency list. For example, the following
describes a situation where 0 is friends with 1 and 2, 3 is
friends with 6, and so on.
{0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]}

Each student can be placed in a friend group, which can be defined
as the transitive closure of that student's friendship relations.
In other words, this is the smallest set such that no student in
the group has any friends outside this group. For the example above,
the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}. Given a friendship
list such as the one above, determine the number of friend groups in the class.
"""


def dfs(graph: dict, src: int, visited: set) -> set:
    visited.add(src)

    for neighbor in graph[src]:
        if neighbor not in visited:
            visited = dfs(graph, neighbor, visited)

    return visited


def friend_groups(graph: dict) -> int:
    visited = set()
    count = 0

    for src in range(len(graph)):
        if src not in visited:
            dfs(graph, src, visited)
            count += 1

    return count


if __name__ == "__main__":
    assert (
        friend_groups({0: [1, 2], 1: [0, 5], 2: [0], 3: [6], 4: [], 5: [1], 6: [3]})
        == 3
    )
