from sympy import *
x = symbols('x')
print(integrate(exp(-x), (x, 0, oo)))
