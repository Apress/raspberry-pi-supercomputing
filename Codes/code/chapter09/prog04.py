from sympy import *

x, y = symbols('x y')
expr = x + y
print(expr.subs({x: 3, y: 2}))
