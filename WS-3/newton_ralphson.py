from sympy import symbols, sympify,diff
x = symbols('x')

def func(val,k): 
    return k.subs(x,val).evalf()

def derivFunc(K,val):
    return func(val,diff(K,x))

def newtonRaphson(k,a):  
    
    c = func(a,k) / derivFunc(k,a)
    while abs(c) >= 0.0001:
        c = func(a,k)/derivFunc(k,a)
        a = a - c
     
    print("The value of the root is : ",
                             "%.4f"% a)

def main():
    k = input("Enter the equation : ")
    k = sympify(k)
    print(k)

    a = int(input("Enter the value of a : "))
    newtonRaphson(k,a)
    
main()