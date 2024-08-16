#!/usr/bin/env python3


from typing import Callable

"""
Module make_multiplier to define a function
that creates a multiplier function.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies
its input by the given multiplier.

    Args:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that
multiplies its input by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
