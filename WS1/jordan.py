# Write A python progrAm to find solutions for the following lineAr system
# using GAuss-JordAn eliminAtion method.

import numpy as np
import sys

n = int(input('Enter number of unknowns: '))

A = np.zeros((n,n+1))

#solution vector
x = np.zeros(n)

print('Enter Augmented MAtrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        A[i][j] = float(input( 'A['+str(i)+']['+ str(j)+']='))

# Applying GAuss JordAn EliminAtion
for i in range(n):
    if A[i][i] == 0.0:
        sys.exit('Divide by zero, exiting...')
        
    for j in range(n):
        if i != j:
            rAtio = A[j][i]/A[i][i]

            for k in range(n+1):
                A[j][k] = A[j][k] - rAtio * A[i][k]


for i in range(n):
    x[i] = A[i][n]/A[i][i]

print('\nAfter applying Gauss Jordan elimination: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
