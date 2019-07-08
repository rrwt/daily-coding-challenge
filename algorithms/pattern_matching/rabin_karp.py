"""
Rabin Karp algorithm for pattern searching.
    Works by matching hash of current substring with given pattern.
    If a match is found, we proceed with naive check, otherwise no.
    The hash needs to be calculated based on previous hash, for it to be efficient.
    
    hash(text[s+1:s+m]) = (d*(hash(text[s:m-1]) - text[s] * h) + text[s+m]) % q
    where,
        d = Number of characters in alphabet
        q = A prime number
        m = length of pattern
        h = pow(d, m-1) % q

Time Complexity: avg - O(n+m), worst - O(nm)
    Worst case occurs when all substrings match with the hash of pattern
"""

d = 256
q = 101


def calculate_hash(string: str, prev_hash: str, start: int, end: int, h: int) -> str:
    """
    calculate rolling hash
    """
    if prev_hash:
        return (
            d * (prev_hash - (h * ord(string[start - 1])) % q) + ord(string[end])
        ) % q
    else:
        hash_value = 0

        for i in range(start, end + 1):
            hash_value = (d * hash_value + ord(string[i])) % q

        return hash_value


def rabin_karp(text: str, pattern: str) -> None:
    n: int = len(text)
    m: int = len(pattern)
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q  # avoid overflow

    pattern_hash: str = calculate_hash(pattern, "", 0, m - 1, h)
    substr_hash: str = calculate_hash(text, "", 0, m - 1, h)

    i = 0

    while i <= n - m:
        if pattern_hash == substr_hash:
            for j in range(m):
                if pattern[j] != text[i + j]:
                    break
            else:
                print("pattern", pattern, "found at index", i)

        i += 1
        if i <= n - m:
            substr_hash = calculate_hash(text, substr_hash, i, i + m - 1, h)
            substr_hash = (substr_hash + q) % q  # in case of -ve value


if __name__ == "__main__":
    text = "ABABABCABABABCABABABCABABACABABAC"
    pattern = "ABABAC"
    rabin_karp(text, pattern)
    pattern = "AAACAAAAAC"
    rabin_karp(text, pattern)
