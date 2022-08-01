#find the eigen values and eigen vectors using direct method
import sympy as sp

x=sp.var('x')

def eigen_vectors(A,l):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    J=H.nullspace()
    for i in range(len(J)):
        print("Eigen Vector for {} is -> {}".format(l,J[i].tolist()))   
    
def eigen_values(A):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    print("Eigen Value(s) of {} is {}\n".format(A.tolist(),sp.solve(DET,x)))
    L=sp.solve(DET,x)
    for i in L:
        eigen_vectors(A,i)

A=sp.Matrix([[4,0,1],[-2,1,0],[-2,0,1]])
B=sp.Matrix([[1,0,-2],[0,0,0],[-2,0,4]])
C=sp.Matrix([[6,3,-8],[0,-2,0],[1,0,-3]])
D=sp.Matrix([[3,0,0],[-2,7,0],[4,8,1]])

print("\na)")
eigen_values(A)
print("\nb)")
eigen_values(B)
print("\nc)")
eigen_values(C)
print("\nd)")
eigen_values(D)