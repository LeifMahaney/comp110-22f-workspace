"""EX04 - `list` Utility Functions"""
__author__ = "730468655"

def all(list: list[int], variable: int) -> bool:
    index: int = 0
    while index < len(list):
        if list[index] == variable:
            index += 1
        else:
            return False
    return True 



def max(input: list[int]) -> int:
    index: int = 0
    maximum: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while index < len(input):
        if input[index] > maximum:
                maximum = input[index]
                index += 1
        else:
                index += 1
    return maximum 



def is_equal(one: list[int], two: list[int]):
    index: int = 0
    if one != two:
        return False
    while one == two:
        if one[index] == two[index]:
            index += 1
        return True

        