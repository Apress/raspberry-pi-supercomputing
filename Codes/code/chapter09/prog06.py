from sympy import *

expr = sqrt(10)
print(expr.evalf())

print(pi.evalf(20))

x = symbols('x')
expr = sin(2*x)
print(expr.evalf(subs={x: 2.4}))
