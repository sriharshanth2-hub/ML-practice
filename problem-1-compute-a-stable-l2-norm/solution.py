import numpy as np


def solve(x):
    """Implement Compute a Stable L2 Norm from the mathematical contract in README.md."""
    arr = np.asarray(x,dtype = np.float64)
    m = np.max(np.abs(arr))
    if m == 0 :
        return 0.0
    scaled = arr / m
    norm = m * np.sqrt(np.sum(scaled**2))
    return float(norm)
