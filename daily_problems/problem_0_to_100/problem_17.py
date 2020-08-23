"""
Suppose we represent our file system by a string in the following manner:
The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2
containing a file file.ext.
The string
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file
within our file system. For example, in the second example above, the longest absolute path
is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest
absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""
from typing import List, Tuple


def longest_path(dir_str: str) -> str:
    """
    To find the longest path to any dir/file.
    Can be easily modified to get the longest path to just a file

    :param dir_str: Directory string containing the directory structure
    :return: longest directory path (number of characters) to any file
    """

    def util(dirs: List[str], prefix: str) -> Tuple[str, int]:
        nonlocal index, l

        if not dirs:
            return "", 0

        max_len = 0
        return_str = ""

        while index < l:
            cur = dirs[index]

            if cur.startswith(prefix):
                cur = cur.lstrip(prefix)
                index += 1
                sub_str, sub_len = util(dirs, prefix + "\t")

                if sub_len + len(cur) + 1 > max_len:
                    if sub_len:
                        max_len = sub_len + len(cur) + 1
                        return_str = cur + "/" + sub_str
                    else:
                        max_len = len(cur)
                        return_str = cur
            else:
                break

        return return_str, max_len

    if not dir_str:
        return ""

    all_dirs = dir_str.split("\n")
    index: int = 0
    l: int = len(all_dirs)

    return util(all_dirs, "")[0]


if __name__ == "__main__":
    assert longest_path("") == ""
    assert longest_path("dir") == "dir"
    assert longest_path("d\n\ts") == "d/s"
    assert (
        longest_path("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
        == "dir/subdir2/file.ext"
    )
    assert (
        longest_path(
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2"
            "\n\t\t\tfile2.ext"
        )
        == "dir/subdir2/subsubdir2/file2.ext"
    )
