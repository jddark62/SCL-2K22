from sympy import symbols, sympify
x = symbols('x')

def func(val,k): 
    return k.subs(x,val).evalf()

def bisection(k,a,b):
 
    if (func(a,k) * func(b,k) >= 0):
        print("Please give a correct A and B\n")
        return
  
    c = a 
    while (abs(b-a) >= 0.001):
        c = (a+b)/2 
        if (func(c,k) == 0.0):
            break
        if (func(c,k)*func(a,k) < 0):
            b = c
        else:
            a = c
             
    print("The value of root is : ","%.4f"%c)
     



def main():
    k = input("Enter the equation : ")
    k = sympify(k)
    print(k)

    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    bisection(k,a,b)
    
main()