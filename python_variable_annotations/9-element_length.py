#!/usr/bin/env python3
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Given a list of strings, return a list of tuples where each tuple contains
    the string and its length.

    Args:
    lst (List[str]): A list of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples where each tuple contains a string and its length.
    """
    return [(i, len(i)) for i in lst]
