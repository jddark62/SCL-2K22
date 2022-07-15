#Gauss Jacobi Method
import numpy as np
from scipy.linalg import solve

def jacobi(A, b, x, n):
    D = np.diag(A)
    R = A - np.diagflat(D)
    for i in range(n):
        x = (b - np.dot(R, x))/D
    return x

A = np.array([[1, -1, 0], [0, 1, -1], [0, 0, 1]])
b = np.array([1, 1, 1])
x = np.array([0, 0, 0])
n = 100
x = jacobi(A, b, x, n)
print(solve(A, b))