import numpy as np
n = int(input("enter the number of data points "))
x = np.zeros(n)
y = np.zeros(n)
print("enter the values in the dataset")
for i in range(0,n):
    x[i] = float(input("x coordinate:"))
    y[i] = float(input("y coordinate:"))
    
Y = float(input("enter the value to be interpolated:"))
l =1
f =0
for i in range(n):
    l=1
    for j in range(n):
        
        if j != i :
            l = l *((Y - y[j])/(y[i] - y[j]))
    f = f + (l*x[i])
    
print("the interpolated value for x = ",Y,"is:",f)

