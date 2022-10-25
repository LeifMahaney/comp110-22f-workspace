"""Dictionary Functions."""

__author__ = "730468655"


def invert(x: dict[str, str]) -> dict[str, str]:
    """This function will take in two strings and invert them."""
    result: dict[str, str] = {}
    for key in x:
        if x[key] in result:
            raise KeyError("Same key used.")
        else:
            result[x[key]] = key
    return result


def favorite_color(names: dict[str, str]) -> str:
    """This function will take two strings and return one string with the most frequent color first."""
    result: str = ""
    values: dict[str, int] = {}
    i: int = 0
    for key in names:
        if names[key] in values:
            values[names[key]] += 1
        else:
            values[names[key]] = 1
    for key in values:
        if i < values[key]:
            i = values[key]
            result = key
    return result


def count(x: list[str]) -> dict[str, int]:
    """This function takes a list and returns a dict with the counts of each item in the list."""
    result: dict[str, int] = {}
    for key in x:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result