import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = []

    for xs in x:
        if xs == 0:
            pmf.append(1-p)
        else:
            pmf.append(p)

    var = float((1-p) * p)

    return  {"pmf":np.asarray( pmf), "mean":float(p), "variance": var}