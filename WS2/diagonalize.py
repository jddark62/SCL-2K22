# Write a python program to diagonalize the following matrix.
import sympy as sp
import numpy as np
x=sp.var('x')

def eigen_vector(mat,l):
    length=mat.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=mat-Z
    J=H.nullspace()
    return J
    
def eigen_value(mat):
    length=mat.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=mat-Z
    Det=H.det()
    print("Diagonlisation of {} is \n".format(mat.tolist()))
    L=sp.solve(Det,x)
    l=[]
    for i in L:
        k=eigen_vector(mat,i)

        for j in range(len(k)):
            l.append(k[j].tolist()) 
    M=np.empty((mat.shape[0],len(l)))
    for i in range(len(l)):
        for j in range(mat.shape[0]):
            M[j][i]=l[i][j][0]
    
    Mi=np.linalg.inv(M)
    #print(M)
    K=Mi.dot(mat)
    K=K.dot(M)
    print(K)
    
            
mat1=sp.Matrix([[1,0],[6,-1]])
mat2=sp.Matrix([[2,0,-2],[0,3,0],[0,0,3]])
mat3=sp.Matrix([[-1,7,-1],[0,1,0],[0,15,-2]])


p,d = mat3.diagonalize()
print(d)

#eigen_value(mat1)
#eigen_value(mat2)
eigen_value(mat3)