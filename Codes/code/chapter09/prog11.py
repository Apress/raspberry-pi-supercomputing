from sympy import *
x = symbols('x')
print(diff(x**3 - x**2 + x, x))
print(diff(x**5, x))
print(diff(sin(x), x))
