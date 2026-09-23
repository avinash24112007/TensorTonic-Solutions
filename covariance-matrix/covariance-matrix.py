import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    Xc = X - np.mean(X, axis=0)

    return np.dot(Xc.T, Xc) / (len(X) - 1)