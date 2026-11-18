import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    import numpy as np
    X = np.array(X)
    out = []
    if axis == 0:
        for row in X.T:
            if (row.max() - row.min()) == 0:
                row = np.zeros(len(row))
            else:
                row = (row - row.min()) / (row.max() - row.min())

            out.append(row)
        out = np.array(out).T
    else:
        for row in X:
            if (row.max() - row.min()) == 0:
                row = np.zeros(len(row))
            else:
                row = (row - row.min()) / (row.max() - row.min())
            out.append(row)

    return np.array(out, dtype=float)