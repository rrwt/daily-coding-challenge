"""
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom
right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:
t     a     g
 h   s z   a
  i i   i z
   s     g
"""


def print_zig_zag(text: str, k: int) -> None:
    size = len(text)
    output = [[" "] * size for _ in range(k)]
    height = 0
    direction = True

    for index in range(size):
        output[height][index] = text[index]
        if direction is True:
            if height < k - 1:
                height += 1
            else:
                direction = False
                height = height - 1
        elif direction is False:
            if height > 0:
                height -= 1
            else:
                direction = True
                height += 1

    for index in range(k):
        print("".join(output[index]))

    print("-" * size)


if __name__ == "__main__":
    print_zig_zag("thisisazigzag", 1)
    print_zig_zag("thisisazigzag", 2)
    print_zig_zag("thisisazigzag", 3)
    print_zig_zag("thisisazigzag", 4)
    print_zig_zag("thisisazigzag", 5)
