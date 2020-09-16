"""
You are given N identical eggs and access to a building with k floors.
Your task is to find the lowest floor that will cause an egg to break,
if dropped from that floor. Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor, you can assume it will also
break when dropped from any floor greater than x.
Write an algorithm that finds the minimum number of trial drops it will take,
in the worst case, to identify this floor.
For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor,
beginning with the first, until we reach the fifth floor, so our solution will be 5.
"""


def egg_drop_problem(num_eggs: int, num_floors: int) -> int:
    """
    Time Complexity: O(n*k*k)
    Space Complexity: (n*k)
    """
    dp = [[0] * (num_floors + 1) for _ in range(num_eggs + 1)]

    for floor in range(1, num_floors + 1):
        dp[1][floor] = floor

    for eggs in range(1, num_eggs + 1):
        dp[eggs][1] = 1

    for eggs in range(2, num_eggs + 1):
        for floor in range(2, num_floors + 1):
            drops = num_floors

            for k in range(1, floor):
                # 1. breaks: remaining floors = k - 1 & remaining eggs = eggs - 1
                # 2. doesn't break: floors = floor - k & remaining eggs = eggs
                drops = min(drops, 1 + max(dp[eggs - 1][k - 1], dp[eggs][floor - k]))

            dp[eggs][floor] = drops

    return dp[num_eggs][num_floors]


if __name__ == "__main__":
    assert egg_drop_problem(2, 100) == 14
    assert egg_drop_problem(2, 36) == 8
    assert egg_drop_problem(1, 5) == 5
