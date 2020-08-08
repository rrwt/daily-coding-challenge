"""
Given a mapping of digits to letters (as in a phone number),
and a digit string, return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.
"""

mapping = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


def get_phone_mapping(text: str) -> list:
    """
    Time Complexity: O(3^n) on average
    Space Complexity: O(3^(n+1)) ?
    """
    if not text:
        return [""]

    number = text[0]
    result = []

    for phone_map in get_phone_mapping(text[1:]):
        for char in mapping[number]:
            result.append(char + phone_map)

    return result


if __name__ == "__main__":
    print(get_phone_mapping("23"))
