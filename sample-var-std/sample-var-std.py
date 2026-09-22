import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean = np.mean(x)

    x = np.asarray(x)

    sums = sum((x-mean) **2 )
    var = float(sums/(len(x) - 1))
    std_div = var**0.5

    return {
        "variance": var,
        "standard_deviation": std_div
    }