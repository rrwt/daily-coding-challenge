"""
A rule looks like this:
A NE B means this means point A is located northeast of point B.
A SW C means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate.
For example:
    A N B
    B NE C
    C N A
    does not validate, since A cannot be both north and south of C.

    A NW B
    A N B
    is considered valid.
"""
from collections import defaultdict
from typing import List


opposite_dir = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
}


def default_dir_map() -> dict:
    return {
        "N": set(),
        "S": set(),
        "E": set(),
        "W": set(),
    }


def add_rules_to_dict(rules: List[str], dir_map: dict) -> dict:
    """
    Construct the rule dictionary
    """
    for rule in rules:
        first, directions, second = rule.split(" ")

        if second not in dir_map:
            dir_map[second] = default_dir_map()

        for direction in directions:
            dir_map[second][direction].add(first)

    return dir_map


def is_valid_direction(
    direction: str, cur_node: str, dir_map: dict, visited: set
) -> bool:
    if cur_node in visited:
        return False

    visited.add(cur_node)

    if direction not in dir_map[cur_node]:
        return True

    for second in dir_map[cur_node][direction]:
        if second in dir_map[cur_node][opposite_dir[direction]] or (
            second in dir_map
            and not is_valid_direction(direction, second, dir_map, visited)
        ):
            return False

    return True


def validate_directions(rules: List[str]) -> bool:
    dir_map = add_rules_to_dict(rules, defaultdict(dict))

    for direction in ("N", "S", "E", "w"):
        visited = set()

        for cur_node in dir_map:
            if not is_valid_direction(direction, cur_node, dir_map, visited):
                return False

    return True


if __name__ == "__main__":
    assert validate_directions(["A N B", "B NE C", "C N A"]) is False
    assert validate_directions(["A NW B", "A N B"]) is True
    assert validate_directions(["A W B", "A N B", "A S B"]) is False
