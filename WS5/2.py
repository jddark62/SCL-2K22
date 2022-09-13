import numpy as np
n = int(input("enter the number of data points "))
x = np.zeros(n)
y = np.zeros(n)
print("enter the values in the dataset")
for i in range(0,n):
    x[i] = int(input("x coordinate:"))
    y[i] = int(input("y coordinate:"))
    
X = int(input("enter the value to be interpolated:"))
l =1
f =0
for i in range(n):
    l=1
    for j in range(n):
        
        if j != i :
            l = l *((X - x[j])/(x[i] - x[j]))
    f = f + (l*y[i])
    
print("the interpolated value for x = ",X,"is:",f)