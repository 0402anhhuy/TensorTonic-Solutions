import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    n = len(y_pred)
    y_pred, y_true = np.asarray(y_pred, dtype=float), np.asarray(y_true, dtype=float)

    return (np.sum((y_true - y_pred)**2)) / n