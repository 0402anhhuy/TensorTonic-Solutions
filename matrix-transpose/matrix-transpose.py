import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    m = len(A)
    n = len(A[0])

    transpose = [];
    for i in range(0, n):
        new_row = []
        for j in range(0, m):
            new_row.append(A[j][i])
        transpose.append(new_row)

    return np.array(transpose)