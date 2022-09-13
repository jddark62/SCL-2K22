import numpy as np
import math
N=int(input("Enter number of unknowns:"))
x=np.zeros(N)
y=np.zeros(N)
delta=np.zeros(N-1)
delta_square=np.zeros(N-2)
delta_third=np.zeros(N-3)
delta_four=np.zeros(N-4)
f_x=pos=final=0
num=val=1

for i in range(0,N):
    print("Enter x value:")
    x[i]=float(input())
    print("Enter y value:")
    y[i]=float(input())
h=x[1]-x[0]
value=float(input("Enter value:"))

for i in range(1,N):
        if value>x[i-1] and value<x[i]:
            pos=x[i-1]
            loc=i-1
            break
if pos==0:
    pos=x[N-1]
    loc=N-1
p=(value-pos)/h

for i in range(0,N-1):
    if i+1<N:
        delta[i]=y[i+1]-y[i]   
 
for i in range(0,len(delta)):
    if i+1<len(delta):
        delta_square[i]=delta[i+1]-delta[i]
        
for i in range(0,len(delta_square)):
    if i+1<len(delta_square):
        delta_third[i]=delta_square[i+1]-delta_square[i]
        
for i in range(0,len(delta_third)):
    if i+1<len(delta_third):
        delta_four[i]=delta_third[i+1]-delta_third[i]
delta_y=np.zeros(N)
if loc<N/2:
    delta_y[0]=y[loc]
    delta_y[1]=delta[loc]
    delta_y[2]=delta_square[loc]
    delta_y[3]=delta_third[loc]
    delta_y[4]=delta_four[loc]
    val=1
    final=0
    for i in range(0,N):
        val=1
        for j in range(0,i):
            val=val*(p-j)
        val=val/math.factorial(i)
        final=final+val*delta_y[i]
    
else:
    delta_y[0]=y[loc]
    delta_y[1]=delta[loc-1]
    delta_y[2]=delta_square[loc-2]
    delta_y[3]=delta_third[loc-3]
    delta_y[4]=delta_four[loc-4]
 
    val=1
    final=0
    for i in range(0,N):
        val=1
        for j in range(0,i):
            val=val*(p+j)
        val=val/math.factorial(i)
        final=final+val*delta_y[i]
   
print(final)





