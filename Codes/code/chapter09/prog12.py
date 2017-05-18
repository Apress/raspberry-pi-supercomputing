from sympy import *
x = symbols('x')
print(diff(10*x**4, x, x, x))
print(diff(10*x**4, x, 3))
