from math import isclose
import sympy as sp
x = sp.symbols('x')


def fixed_point_method(F, a, b):
    f = sp.sympify(F())
    f_dash = sp.diff(f, x)
    if(max(abs(f_dash.subs(x, a)), abs(f_dash.subs(x, b))) > 1):
        return "no roots"
    x_n = a
    for i in range(10):
        x_n1 = f.subs(x, x_n)
        if (isclose(x_n, x_n1)):
            break
        x_n = x_n1
    return "The root is : {}".format(x_n1.evalf())


#a
def Qa(): return 'cos(x)*((2.7182)**(x))'
print("a  => {}".format(fixed_point_method(Qa, 0.5, 0.55)))

#b
def Qb(): return 'cos(x) - 3*x + 1'
print("b  => {}".format(fixed_point_method(Qb, 1.84, 1.86)))

#c
def Qc(): return '(2.7182)**(-x)'
print("c  => {}".format(fixed_point_method(Qc, 0.5, 0.6)))

#d
def Qd(): return '(x**2 + 2 + 1/((2.7182)**(-x)))/5'
print("d  => {}".format(fixed_point_method(Qd, 1, 2)))

#e
def Qe(): return 'sin(x)+ 0.5'
print("e  => {}".format(fixed_point_method(Qe, 1.4, 1.6)))

#f
def Qf(): return '10**((2.7182)**(-x)/3)'
print("f  => {}".format(fixed_point_method(Qf, 1.2, 1.3)))

#g
def Qg(): return ' x*acos(0) - 2*acos(0)'
print("g  => {}".format(fixed_point_method(Qg, 5.5, 5.6)))