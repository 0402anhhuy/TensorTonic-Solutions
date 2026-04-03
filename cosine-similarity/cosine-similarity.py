import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    dot_product = np.dot(a, b)
    Euclidean_norms_a = np.sqrt(np.sum(a**2))
    Euclidean_norms_b = np.sqrt(np.sum(b**2))
    if Euclidean_norms_a * Euclidean_norms_b == 0.0:
        return 0.0
    return dot_product / (Euclidean_norms_a * Euclidean_norms_b)