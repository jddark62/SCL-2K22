# Write a python program for Gauss-Jordan Elimination method to find
# the RREF of the following matrices.
def rref( M):
    if not M: return
    lead = 0
    row_count = len(M)
    column_count = len(M[0])
    for r in range(row_count):
        if lead >= column_count:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == row_count:
                i = r
                lead += 1
                if column_count == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(row_count):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
 
 
matrix = [
   [ 1, 2, -1, -4],
   [ 2, 3, -1, -11],
   [-2, 0, -3, 22],]
 
rref( matrix )
 
for rw in matrix:
    print (', '.join( (str(rv) for rv in rw) ))