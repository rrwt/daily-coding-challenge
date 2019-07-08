"""
Naive pattern matching
Time Complexity: O(n*(m-n+1))
    worst case: When almost all character match at all points
    best case: When first character does not match - O(m)
"""


def match(text: str, pattern: str) -> None:
    m, n = len(text), len(pattern)

    for i in range(m - n + 1):
        if text[i] == pattern[0]:
            matched = text[i : i + n] == pattern
            if matched:
                print(pattern, "found at index", i, "of", text)
                return

    print(pattern, "not found in", text)


if __name__ == "__main__":
    match("AABCCAADDEE", "FAA")
    match("AABCCAADDEE", "BCCAA")
    match("AABCCAADDEE", "DEE")
