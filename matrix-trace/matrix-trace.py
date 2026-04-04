import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    n, sum = len(A), 0
    for i in range(n):
        sum += A[i][i]

    return sum