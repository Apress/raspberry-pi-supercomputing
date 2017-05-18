from sympy import *
x, y = symbols('x y')
print(integrate(exp(-x)*exp(-y), (x, 0, oo), (y, 0, oo)))
