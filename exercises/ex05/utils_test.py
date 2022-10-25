"""Test for Utils."""
from utils import only_evens, concat, sub
__author__ = "730468655"


def test_only_evens_empty_list() -> None:
    """Edge case - returns empty if list empty."""
    xs: list[int] = []
    assert only_evens(xs) == []
    
    
def test_only_for_mixed_list() -> None:
    """Use case - tests it returns only evens for a large list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(xs) == [2, 4, 6]
    
    
def test_only_evens_all_odd() -> None: 
    """Use case - tests returns empty if all items odd."""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []
    
    
def test_concact_two_different_lists() -> None:
    """Use case - returns one list of ints and then the latter list right after that."""
    list1: list[int] = [0, 1, 2, 3, 4, 5]
    list2: list[int] = [6, 7, 8, 9, 10]
    assert concat(list1, list2) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    
def test_concact_two_equal_lists() -> None:
    """Use case - return one list by adding two identical lists."""
    list1: list[int] = [2, 2, 2, 2]
    list2: list[int] = [2, 2, 2, 2]  
    assert concat(list1, list2) == [2, 2, 2, 2, 2, 2, 2, 2]
    
    
def test_one_list_of_ints_one_list_empty() -> None:
    """Edge case - return only the list of ints."""  
    list1: list[int] = [1, 2, 3, 4]
    list2: list[int] = []
    assert concat(list1, list2) == [1, 2, 3, 4]
    
    
def test_sub_list_of_wide_range_numbers() -> None:
    """Use case - return a subset of the main list."""
    xs: list[int] = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
    assert sub(xs, 1, 8) == [90, 80, 70, 60, 50, 40, 30]
    
    
def test_sub_list_start_greater_then_len_of_list() -> None:
    """Use case - returns an empty list."""
    xs: list[int] = [1, 1, 1, 1]
    assert sub(xs, 5, 4) == []
    
    
def test_sub_list_start_index_is_negative() -> None:
    """Edge case - return the beginning of the list to the end index determined by the range."""
    xs: list[int] = [1, 2, 1, 2]
    assert sub(xs, -1, 3) == [1, 2, 1]