"""
Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary.
If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example,
    given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
    and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

    Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')]
    and starting airport 'COM', you should return null.

    Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
    even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
    However, the first one is lexicographically smaller.
"""
from typing import List, Tuple


def backtrack_fi(itineraries: List[Tuple[str, str]], start: str) -> list:
    if not itineraries:
        return [start]

    for index, (s, e) in enumerate(itineraries):
        if s == start:
            return_list = [start] + backtrack_fi(
                itineraries[:index] + itineraries[index + 1:], e
            )

            if len(return_list) == len(itineraries) + 1:
                return return_list

    return []


def flight_itinerary(itineraries: List[Tuple[str, str]], start: str) -> List[str]:
    # sort input for lexicographic results
    itineraries.sort(key=lambda airport: airport[0] + airport[1])
    return backtrack_fi(itineraries, start)


if __name__ == "__main__":
    print(
        flight_itinerary(
            [("SFO", "HKO"), ("YYZ", "SFO"), ("YUL", "YYZ"), ("HKO", "ORD")], "YUL"
        )
    )
    print(flight_itinerary([("SFO", "COM"), ("COM", "YYZ")], "COM"))
    print(flight_itinerary([("A", "B"), ("A", "C"), ("B", "C"), ("C", "A")], "A"))
