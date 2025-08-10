from __future__ import annotations
from typing import Callable, Tuple

def build(n1: float, n2: float) -> Tuple[float, float, float, Callable[[float], float], Callable[[float], float]]:
    """Return (a, b, c, p2c, jac_p2c) where:
       a = n1 + n2
       b = n1 - n2
       c = 2*n1 - n2
       p2c(x) = a*x**2 + b*x + c
       jac_p2c(x) = 2*a*x + b
    """
    a = n1 + n2
    b = n1 - n2
    c = 2 * n1 - n2

    def p2c(x: float) -> float:
        return a * x**2 + b * x + c

    def jac_p2c(x: float) -> float:
        return 2 * a * x + b

    return a, b, c, p2c, jac_p2c