"""
Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the person's
itinerary. If no such itinerary exists, return null.
All flights must be used in the itinerary.

For example, given the following list of flights:

    HNL ➔ AKL
    YUL ➔ ORD
    ORD ➔ SFO
    SFO ➔ HNL

and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL.
Notice that a greedy solution won't work, since it's possible to have a cycle in the graph.
"""


def flight_itinerary(flights: list, itinerary: list, num_flights: int) -> None:
    if not flights:
        return

    for i, (origin, dest) in enumerate(flights):
        if not itinerary:
            itinerary.append(origin)

        if itinerary[-1] == origin:
            itinerary.append(dest)
            flight_itinerary(flights[:i] + flights[i + 1 :], itinerary, num_flights)

            if 1 + num_flights == len(itinerary):
                return

            itinerary.pop()

        if len(itinerary) == 1:
            itinerary.pop()


if __name__ == "__main__":
    res: list = []
    flight_itinerary(
        [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")], res, 4
    )

    print(*res, sep="->")
