"""Dictionary related utility functions."""

__author__ = "730468655"

# Define your functions below

from csv import DictReader


def read_csv_rows(path: str) -> list[dict[str, str]]:
    """This function is supposed to read data and compute it into a dict."""
    result: list[dict[str, str]] = []
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for key in csv_reader:
        result.append(key)
    file_handle.close()
    return result 


def column_values(x: list[dict[str, str]], y: str) -> list[str]:
    """Creates a list of strings that are the values in the single column."""
    result: list[str] = []
    for key in x:
        value: str = key[y]
        result.append(value)
    return result 


def columnar(x: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a table of a list into a dict."""
    result: dict[str, list[str]] = {}
    first: dict[str, str] = x[0]
    for key in first:
        result[key] = column_values(x, key)
    return result
        
        
def head(x: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Create a new column with only the first paramter of each column."""
    result: dict[str, list[str]] = {}
    for key in x:
        if y > len(x[key]):
            y = len(x[key])
        new: list[str] = []
        i: int = 0
        while i < y:
            new.append(x[key][i])
            i += 1
        result[key] = new
    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Create a new table with a specific set of columns."""
    result: dict[str, list[str]] = {}
    for key in y:
        if key in y:
            result[key] = x[key]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new table with two tables combined."""
    result: dict[str, list[str]] = {}
    for key in x:
        result[key] = x[key]
    for key in y:
        if key in result:
            i: int = 0
            while i < len(y[key]):
                result[key].append(y[key][i])
                i += 1
        else:
            result[key] = y[key]
    return result


def count(x: list[str]) -> dict[str, int]:
    """Will create a dict when given a list with unique key values as well as a count."""
    result: dict[str, int] = {}
    for key in x:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result
            
            