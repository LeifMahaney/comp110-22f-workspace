"""Using Lists with Directorys."""

__author__ = "730468655"


def only_evens(input: list[int]) -> list[int]:
    """Is a list that returns only the even integers in the list."""
    total: list[int] = list()
    i: int = 0
    while i < len(input):
        if input[i] % 2 == 0:
            total.append(input[i])
        i += 1
    return total
        

def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Creates a new list that returns the first list and than the second list."""
    list_concat: list[int] = list()
    i: int = 0
    while i < len(list_1):
        list_concat.append(list_1[i])
        i += 1
    i = 0
    while i < len(list_2):
        list_concat.append(list_2[i])
        i += 1
    return list_concat


def sub(list_1: list[int], start: int, end: int) -> list[int]:
    """When given a list it will return the values between (end-1) - start."""
    sublist: list[int] = list()
    if start < 0:
        start = 0
    if end > len(list_1):
        end = len(list_1)
    if len(list_1) == 0 or start >= len(list_1) or end <= 0:
        return []
    while start < end:
        sublist.append(list_1[start])
        start += 1
    return sublist