import numpy as np

sigma = 0.0


def oracle(x):
    return np.sin(7 * x) + np.cos(15 * x)
