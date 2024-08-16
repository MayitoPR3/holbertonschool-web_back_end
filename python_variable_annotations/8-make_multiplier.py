#!/usr/bin/env python3


from typing import Callable

"""
function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier.
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
