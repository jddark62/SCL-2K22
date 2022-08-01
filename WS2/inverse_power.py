import numpy as np

row=int(input("Enter row size : "))
col=int(input("Enter col size : "))
a_matrix=np.zeros((row,col))
a_inv_matrix=np.zeros((row,col))
x_matrix=np.zeros((row,1))
x1_matrix=np.zeros((row,1))
n=0
print("\nEnter array elements")
for i in range(0,row):
    for j in range(0,col):
        a_matrix[i][j]=int(input())
print("\nEnter intial matrix")
for i in range(0,row):
    x_matrix[i][0]=int(input())
   
a_inv_matrix=np.linalg.inv(a_matrix).copy()
while n<6:
    x1_matrix=np.dot(a_inv_matrix,x_matrix)
    x_matrix=x1_matrix.copy()
    n=n+1;
print("\nDominant Eigenvector")
for i in range(0,row):
    print(x_matrix[i][0]," ")
    
   
value=(np.dot(a_inv_matrix,x_matrix)*x_matrix)
value1=x_matrix*x_matrix
print("\nDominant Eigenvalue")
print(value/value1)