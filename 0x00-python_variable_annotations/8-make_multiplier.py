#!/usr/bin/env python3

""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float by the multiplier """
    def multiply(n: float) -> float:
        """ Multiplies a float by the multiplier """
        return float(n * multiplier)

    return multiply
