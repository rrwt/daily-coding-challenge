"""
You are given a list of data entries that represent entries and exits of
groups of people into a building. An entry looks like this:
    {"timestamp": 1526579928, count: 3, "type": "enter"}
    This means 3 people entered the building. An exit looks like this:

    {"timestamp": 1526580382, count: 2, "type": "exit"}
    This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building.
Return it as a pair of (start, end) timestamps. You can assume the building always starts off
and ends up empty, i.e. with 0 people inside.
"""
from typing import List


def busiest_period(entries: List[dict]) -> int:
    entries.sort(key=lambda x: x["timestamp"])

    count_max = 0
    cur_count = 0
    max_timestamp = 0

    for entry in entries:
        if entry["type"] == "enter":
            cur_count += entry["count"]

            if cur_count > count_max:
                count_max = cur_count
                max_timestamp = entry["timestamp"]
        else:
            cur_count -= entry["count"]

    return max_timestamp


if __name__ == "__main__":
    print(
        busiest_period(
            [
                {"timestamp": 1526579928, "count": 3, "type": "enter"},
                {"timestamp": 2526579928, "count": 3, "type": "enter"},
                {"timestamp": 3526579928, "count": 3, "type": "enter"},
                {"timestamp": 1426579928, "count": 3, "type": "enter"},
                {"timestamp": 1516379928, "count": 3, "type": "enter"},
                {"timestamp": 1526579628, "count": 3, "type": "exit"},
                {"timestamp": 1526879928, "count": 3, "type": "exit"},
                {"timestamp": 2526579528, "count": 3, "type": "exit"},
            ]
        )
    )
