"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


# O(n) and constant space
def largest_non_adjacent_sum(input_list):
    if not input_list:
        return None

    length = len(input_list)

    if length == 1:
        return input_list[0]

    max_sum_inc_cur = input_list[0]
    max_sum_exc_cur = 0

    for elem in input_list[1:]:
        temp = max(max_sum_exc_cur, max_sum_exc_cur + elem, elem)
        max_sum_exc_cur = max(max_sum_inc_cur, max_sum_exc_cur)
        max_sum_inc_cur = temp

    return max(max_sum_inc_cur, max_sum_exc_cur)
