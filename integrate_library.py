import numpy as np


def integrate(function_to_integrate, from_x, to_x, num_elements):
    n = num_elements
    a = from_x
    b = to_x

    dx = (b - a) / n
    xk_star = np.linspace(a, b, n, endpoint=False) + dx/2
    f_xk_star = function_to_integrate(xk_star)
    sum = np.sum(f_xk_star) * dx
    return sum
