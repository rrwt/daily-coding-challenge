"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
    {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    it should become:
    {
        "key": 3,
        "foo.a": 5,
        "foo.bar.baz": 8
    }
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""
from typing import Optional


def flatten_dict(original: dict, prefix: Optional[str] = "") -> dict:
    return_dict = {}

    for key, value in original.items():
        pref_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            return_dict.update(flatten_dict(value, pref_key))
        else:
            return_dict[pref_key] = value

    return return_dict


if __name__ == "__main__":
    assert flatten_dict({"key": 3, "foo": {"a": 5, "bar": {"baz": 8}}}) == {
        "key": 3,
        "foo.a": 5,
        "foo.bar.baz": 8,
    }
