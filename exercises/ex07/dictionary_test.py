"""Test for Dictionary."""
from dictionary import invert, favorite_color, count
__author__ = "730468655"


def test_invert_empty_dict() -> None:
    """Edge case to see if an empty dict is returned when inverted."""
    result: dict[str, str] = {}
    assert invert(result) == {}
    

def test_invert_individual_key() -> None:
    """Use case that takes an individual key and  inverts it."""
    result: dict[str, str] = {"Tom": "Jerry"}
    assert invert(result) == {"Jerry": "Tom"}


def test_invert_multiple_keys() -> None:
    """Use case that takes multiple keys and inverts all of them in order."""
    result: dict[str, str] = {"Jake": "State", "Chicken": "Fried", "State": "Fair"}
    assert invert(result) == {"State": "Jake", "Fried": "Chicken", "Fair": "State"}


def test_favorite_color_tie_for_best_color() -> None:
    """Use case that when given two colors of equal inputs, the color that appeard first will print."""
    result: dict[str, str] = {"Jake": "Red", "Leif": "Red", "Lebron": "Blue", "Shaq": "Blue"}
    assert favorite_color(result) == "Red"


def test_favorite_color_empty_str() -> None:
    """Edge case used to see if an empty str is returned."""
    result: dict[str, str] = {}
    assert favorite_color(result) == ""
    
    
def test_favorite_color_all_chose_same_color() -> None:
    """Use case that when given only one color will generate only that color."""
    result: dict[str, str] = {"Jake": "Pink", "Leif": "Pink", "Lebron": "Pink", "Shaq": "Pink"}
    assert favorite_color(result) == "Pink"


def test_count_equal_index() -> None:
    """Use case that when given mutiple inputs of the same index, the."""
    result: list[str] = ['J', 'J', 'L', 'L', 'J', 'M', 'L', 'M', 'M']
    assert count(result) == {"J": 3, "L": 3, "M": 3}
    

def test_count_normal_list() -> None:
    """Use case that takes a normal list and returns count of items in input list."""
    correct: list[str] = ["J", "J", "L", "L", "J", "M"]
    assert count(correct) == {"J": 3, "L": 2, "M": 1}
    
        
def test_count_empty_list_dict() -> None:
    """Edge case used to see if an empty dict is returned."""
    values: list[str] = []
    assert count(values) == {}