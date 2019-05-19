""""
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the
additional characters,and that you are given the "true" length of the string.
"""


# O(n)


def urlify(str_in):
    return "%20".join(str_in.strip().split())


if __name__ == "__main__":
    print(urlify("     he  is    a     brave   knight    "))
