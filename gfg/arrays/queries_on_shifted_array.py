"""
Given an array A of N integers. There are three type of type of commands:

1 x : Right Circular Shift the array x times. If an array is a[0], a[1], …., a[n – 1],
    then after one right circular shift the array will become a[n – 1], a[0], a[1], …., a[n – 2].
2 y : Left Circular Shift the array y times. If an array is a[0], a[1], …., a[n – 1],
    then after one right circular shift the array will become a[1], …., a[n – 2], a[n – 1], a[0].
3 l r : Print the sum of all integers in the subarray a[l…r] (l and r inclusive).

Given Q queries, the task is execute each query.
"""


class Queries:
    def __init__(self, arr: list):
        self.start: int = 0
        self.arr_len: int = len(arr)
        self.arr: list = arr * 2

    def queries(self, q_type: int, *args) -> None:
        if q_type == 1:
            self.start -= args[0]
            if self.start < 0:
                self.start %= self.arr_len
        elif q_type == 2:
            self.start += args[0]

            if self.start >= self.arr_len:
                self.start %= self.arr_len
        elif q_type == 3:
            print(sum(self.arr[self.start + args[0] : self.start + args[1] + 1]))
        else:
            raise AssertionError("Invalid Query")


if __name__ == "__main__":
    q = Queries([1, 2, 3, 4, 5])
    q.queries(1, 3)
    q.queries(3, 0, 2)
    q.queries(2, 1)
    q.queries(3, 1, 4)
