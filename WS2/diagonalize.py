# Write a python program to diagonalize the following matrix.
import sympy as sp
import numpy as np

x=sp.var('x')

def eigen_vectors(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    return J
    
def eigen_values(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    L=sp.solve(DET,x)
    l=[]
    for i in L:
        k=eigen_vectors(A,i)
        for j in range(len(k)):
            l.append(k[j].tolist()) 
    M=np.empty((A.shape[0],len(l)))
    for i in range(len(l)):
        for j in range(A.shape[0]):
            M[j][i]=l[i][j][0]
    N=np.linalg.inv(M)
    K=N.dot(A.tolist())
    K=K.dot(M)
    print("{}\n\nDiagonalized Matrix:".format(A.tolist()))
    print(K.astype(int))
                
A=sp.Matrix([[1,0],[6,-1]])
B=sp.Matrix([[2,0,-2],[0,3,0],[0,0,3]])
C=sp.Matrix([[-1,7,-1],[0,1,0],[0,15,-2]])

print("\na)")
eigen_values(A)
print("\nb)")
eigen_values(B)
print("\nc)")
eigen_values(C)