"""
Given a number in Roman numeral format, convert it to decimal.
The values of Roman numerals are as follows:
{ 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }
In addition, note that the Roman numeral system uses
subtractive notation for numbers such as IV and XL.
For the input XIV, for instance, you should return 14.
"""

roman_nums = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1,
}


def roman_to_decimal(roman: str) -> int:
    index = 0
    size = len(roman)
    val = 0

    while index < size:
        if index < size - 1 and roman[index : index + 2] in roman_nums:
            val += roman_nums[roman[index : index + 2]]
            index += 2
        else:
            val += roman_nums[roman[index]]
            index += 1

    return val


if __name__ == "__main__":
    print(f"XIV -> {roman_to_decimal('XIV')}")
    print(f"MMCDXCIX -> {roman_to_decimal('MMCDXCIX')}")
