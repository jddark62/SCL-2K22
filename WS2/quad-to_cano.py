import sympy as sp
import numpy as np

x = sp.var('x')
y = sp.var('y')
z = sp.var('z')

def calEigVecs(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    return J
    
def calEigVals(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    L=sp.solve(DET,x)
    l=[]
    for i in L:
        k=calEigVecs(A,i)
        for j in range(len(k)):
            l.append(k[j].tolist()) 
    M=np.empty((A.shape[0],len(l)))
    for i in range(len(l)):
        for j in range(A.shape[0]):
            M[j][i]=l[i][j][0]
    N=np.linalg.inv(M)
    K=N.dot(A.tolist())
    K=K.dot(M)
    print("\nSYMMETRIC MATRIX AFTER DIAGONALIZATION IS:")
    return (K.astype(int))
    
def main():    
    n = int(input("Enter the no of variables : "))
    expr = sp.sympify(input("Enter the quadratic form : "))
    symmetric_matrix = [[] for  i in  range(n)]
    if n == 2:
        symmetric_matrix[0].append(expr.coeff(x**2))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(expr.coeff(y**2))
        print("\nSYMMETRIC MATRIX FOR GIVEN QUADRATIC FORM IS:",symmetric_matrix)
        SYMMETRIC=sp.Matrix(symmetric_matrix)
        diag=calEigVals(SYMMETRIC)
        print(diag)
        print("\nCANONICAL FORM FOR GIVEN QUADRATIC FORM IS:")
        print("{}*x**2+{}*y**2".format(diag[0,0],diag[1,1]))
    if n == 3:
        symmetric_matrix[0].append(expr.coeff(x**2))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[0].append(int(0.5*(expr.coeff(x*z))))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(x*y))))
        symmetric_matrix[1].append(expr.coeff(y**2))
        symmetric_matrix[1].append(int(0.5*(expr.coeff(y*z))))
        symmetric_matrix[2].append(int(0.5*(expr.coeff(x*z))))
        symmetric_matrix[2].append(int(0.5*(expr.coeff(y*z))))
        symmetric_matrix[2].append(expr.coeff(z**2))
        print("\n Symmetric matrix after diagonalization is:",symmetric_matrix)
        SYMMETRIC=sp.Matrix(symmetric_matrix)
        calEigVals(SYMMETRIC)
        diag=calEigVals(SYMMETRIC)
        print(diag)
        print("\nCanonical form for given quadratic form:")
        print("{}*x**2+{}*y**2+{}*z**2".format(diag[0,0],diag[1,1],diag[2,2]))
        
main()
