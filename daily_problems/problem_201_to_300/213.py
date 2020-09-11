"""
Given a string of digits, generate all possible valid IP address combinations.
IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.
For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""
from typing import List


def is_valid(num: str) -> bool:
    return -1 < int(num) < 256 and (num[0] != "0" or len(num) == 1)


def _generate_addresses(
    num: str, index: int, size: int, iteration: int
) -> List[List[str]]:
    if index == size:
        return [[]]

    if index > size or iteration > 3:
        return []

    return_list = []

    for length in range(1, min(size - index + 1, 4)):
        cur_list = []
        val = num[index: index + length]

        if is_valid(val):
            for address in _generate_addresses(
                num, index + length, size, iteration + 1
            ):
                cur_list.append([val] + address) if address else cur_list.append([val])

        return_list.extend(cur_list)

    return return_list


def generate_ip_addresses(number: str) -> List[str]:
    addresses = _generate_addresses(number, 0, len(number), 0)
    return [".".join(address) for address in addresses if len(address) == 4]


if __name__ == "__main__":
    assert generate_ip_addresses("2542540123") == ["254.25.40.123", "254.254.0.123"]
    assert generate_ip_addresses("0000") == ["0.0.0.0"]
    assert generate_ip_addresses("255255255255") == ["255.255.255.255"]
    assert generate_ip_addresses("100100110") == [
        "10.0.100.110",
        "100.10.0.110",
        "100.100.1.10",
        "100.100.11.0",
    ]
