"""EX04 - `list` Utility Functions."""
__author__ = "730468655"


def all(list: list[int], variable: int) -> bool:
    """Using the all function, two new varibles are initilized. One a list and one a variable."""
    index: int = 0
    if len(list) == 0:
        return False
    if len(list) == -1:
        return False
    while index < len(list):
        if list[index] == variable:
            index += 1
        else:
            return False
    return True 


def max(input: list[int]) -> int: 
    """Using the max function when given an input we are able to calculate of the numbers in the input which is the max."""
    index: int = 0
    maximum: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while index < len(input):
        if input[index] > maximum:
            maximum = input[index]
            index += 1
        else:
            index += 1
    return maximum 


def is_equal(one: list[int], two: list[int]) -> int: 
    """This function allows us to test whether two lists are equal to one another."""
    index: int = 0
    if len(one or two) == 0:
        return True
    elif one != two:
        return False
    else:
        while one == two:
            if one[index] == two[index]:
                if index == len(one) - 1:
                    return True
                else:
                    index += 1
            return True        
    return False 
        