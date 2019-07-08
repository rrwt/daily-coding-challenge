"""
KMP pattern matching algorithm.
Finds matching patterns in text in linear time.
Text: A longer string of length n. (n > m)
Pattern: Substring to be searched for of length m.
Works by precompiling the pattern string to create a LPS string array.
LPS: Longest Proper Prefix. Longest prefix string that is also a suffix
Time Complexity: O(n+m)
Space Complexity: O(m)
"""


def compute_lps(pattern: str, m: int) -> list:
    """
    Algorithm to compute LPS for given pattern.
    """
    lps = [0] * m
    i, j = 1, 0  # j = length of previous longest prefix-suffix

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            # backtrack j. It cannot suddenly reduce to 0 as we might have a
            # suffix - prefix pair ending at j
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return lps


def kmp(text: str, pattern: str) -> None:
    n, m = len(text), len(pattern)
    lps = compute_lps(pattern, m)

    i, j = 0, 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            print("pattern", pattern, "found at location", i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1


if __name__ == "__main__":
    text = "ABABABCABABABCABABABCABABACABABAC"
    pattern = "ABABAC"
    kmp(text, pattern)
    pattern = "AAACAAAAAC"
    kmp(text, pattern)
