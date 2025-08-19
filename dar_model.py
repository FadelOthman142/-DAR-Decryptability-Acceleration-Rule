import numpy as np

def dar(E, H, alpha, beta, K):
    """Decryptability Acceleration Rule formula."""
    return (K * np.sqrt(E)) / (alpha + beta * np.log2(1 + H))
