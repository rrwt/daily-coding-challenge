"""
Given an absolute pathname that may have . or .. as part of it,
return the shortest standardized path.
For example,
    given "/usr/bin/../bin/./scripts/../",
    return "/usr/bin/".
"""


def standardized_path(path: str) -> str:
    path_list = path.split("/")
    res = []

    for index in range(len(path_list)):
        if path_list[index] == "..":
            res.pop()
        elif path_list[index] != ".":
            res.append(path_list[index])

    return "/".join(res)


if __name__ == "__main__":
    print(standardized_path("/usr/bin/../bin/./scripts/../"))
    print(standardized_path("/usr/bin/./scripts/abc.txt"))
