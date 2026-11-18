def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    import numpy as np    
    data= np.array(data)

    out = []
    for row in data.T:
        if (row.max() - row.min()) == 0:
            row = np.zeros(len(row))
        else:
            row = (row - row.min()) /  (row.max() - row.min())
        out.append(row)
    out = np.array(out).T.tolist()

    
    return out