"""
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaaa would become
a2b1c5a3. If the "compressed" string would not become smaller than the
original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).
"""


# O(n)
def compress(str_in):
    l = len(str_in)
    i = 0
    res = []

    while i < l:
        count = 1
        cur = str_in[i]
        i += 1

        while i < l:
            if str_in[i] != cur:
                break
            count += 1
            i += 1

        res.extend([cur, count])

    res = "".join(res)

    return res if len(res) < l else str_in


if __name__ == "__main__":
    assert compress("aabcccccaaa") == "a2b1c5a3"
