import numpy as np
from integrate_library import integrate

'''IMPORTANT TIP, PLEASE READ! This is useful for the last example.
A function taking a vector of values and returning 1 will *not* return a vector,
but rather a single number. This function solves this silly problem,
and you should use it.
'''
# functions
def constant_function_of_one(x):
    '''Evaluates a constant function returning 1.
    It handles both a single number and np.array as input.

    Args:
      x: either a float or np.array of length n
    Returns:
      either a single 1. (as a float) or a length-n np.array of 1.
    '''
    return 0 * x + 1.

def close_enough(a, b, num_digits):
  return np.abs(a-b) < 10**-num_digits

def f1(x):
  value = np.cos(x) / (1 + 2*np.cos(x))
  return np.arccos(value)

def f2(x):
  value = np.cosh(x)
  return value

def f3(x):
  value = 1 / x
  return value

def extra_case(x):
  value = np.log(x-(x**2))
  return value

# tests
def test_f1():
  cor1 = 5/24 * (np.pi**2)
  res1 = (integrate(f1, 0, np.pi/2, 1000))
  assert close_enough(res1, cor1, num_digits=5)

def test_f2():
  cor2 = (np.e**np.e - np.e**-np.e) / 2
  res2 = integrate(f2, 0, np.e, 1000)
  assert close_enough(res2, cor2, num_digits=5)

def test_f3():
  cor3 = 1.0
  res3 = (integrate(f3, 1.0, np.e, 1000))
  assert close_enough(res3, cor3, num_digits=5)

def test_constant():
  cor4 = 1.0
  res4 = (integrate(constant_function_of_one, 0, 1.0, 1000))
  assert close_enough(res4, cor4, num_digits=5)

def test_extra():
  cor5 = -2.0
  res5 = (integrate(extra_case, 0, 1.0, 100000))
  assert close_enough(res5, cor5, num_digits=5)
