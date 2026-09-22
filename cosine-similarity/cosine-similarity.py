import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here

    a = np.asarray(a)
    b = np.asarray(b)

    if np.linalg.norm(a) * np.linalg.norm(b) == 0:
        return float(0)
    return float(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b)))