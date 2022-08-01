import sympy as sp

x=sp.var('x')

def is_symmetric(a, n):
    for i in range(n):
        for j in range(n):
            if (a[i,j] != a[j,i]):
                return False
    return True

def rank(A):
    count=0
    M=[0,0,0,0]
    for i in range(len(A)):
        if A[i]!=M:
            count=count+1
        else:
            return count

def gauss_jordan(arr):
    i=0
    j=0
    pos=0
    while i<len(arr):
        if arr[i][0]!=0:
            arr[pos],arr[i]=arr[i],arr[pos]
            break
        else:
            i=i+1
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if(arr[i][j]!=0):
                for k in range(0,len(arr)):
                    if i!=k:
                        c=arr[k][j]/arr[i][j]
                        for l in range(0,len(arr[k])):
                            arr[k][l]=arr[k][l]-c*arr[i][l]
                break
    return arr

def eigen_vectors(A,l,count):
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(l)
    H=A-Z
    P=sp.Matrix([[0],[0],[0]])
    H1=H.col_insert(3,P)
    P1=gauss_jordan(H1.tolist())
    C=rank(P1)
    J=H.nullspace()
    if(length-C==len(J)):
        count=count+1 
    return count
    
def eigen_values(A):
    count=0
    length=A.shape[0]
    I=sp.eye(length)
    Z=I.multiply(x)
    H=A-Z
    DET=H.det()
    L=sp.solve(DET,x)
    for i in L:
        count=eigen_vectors(A,i,count)
    if(count==A.shape[0] or is_symmetric(A, 3)):
        print("{} is diagonalizable".format(A.tolist()))
    else:
        print("{} is not diagonalizable".format(A.tolist()))

A=sp.Matrix([[-10,11,-6],[-15,16,-10],[-3,3,-2]])
B=sp.Matrix([[3,-1,0],[-1,2,-1],[0,-1,3]])
C=sp.Matrix([[1,-7,-1],[0,1,0],[0,15,-2]])

print("\na)")
eigen_values(A)
print("\nb)")
eigen_values(B)
print("\nc)")
eigen_values(C)
