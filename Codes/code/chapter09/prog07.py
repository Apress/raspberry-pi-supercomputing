from sympy import *

x = symbols('x')
init_session()
print(Integral(sqrt(1/x), x))
