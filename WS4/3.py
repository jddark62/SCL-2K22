from sympy import *
x = [0,1,2]
y = [0,1,20]

a = var('a')
b = var('b')
c = var('c')
expr = []
for i in range(3):
    expr.append( Eq(a*x[i]**2+b*x[i]+c , y[i]))

res = solve((expr[0],expr[1],expr[2]),(a,b,c))

print("the equation of the parabola is: ",res[a],"x**2+",res[b],"x+",res[c])
