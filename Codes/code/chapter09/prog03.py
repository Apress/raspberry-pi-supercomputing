from sympy import *

x = symbols('x')
expr = x + 1
print(expr.subs(x, 3))
