"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""


def verify_palindrome(number: int) -> bool:
    if number < 10:
        return True

    nums = []

    while number > 0:
        nums.append(number % 10)
        number //= 10

    start, end = 0, len(nums) - 1

    while start < end:
        if nums[start] != nums[end]:
            return False
        start += 1
        end -= 1

    return True


if __name__ == "__main__":
    assert verify_palindrome(121) is True
    assert verify_palindrome(888) is True
    assert verify_palindrome(678) is False
