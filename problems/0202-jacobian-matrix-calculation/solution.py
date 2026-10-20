import numpy as np
import math

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
    base = f(x)
    m = len(base)  # Number of outputs
    n = len(x)     # Number of inputs

    J = [[0.0 for _ in range(n)] for _ in range(m)]

    for j in range(n):
        new_x = x.copy()
        new_x[j] += h

        new_f = f(new_x)

        for i in range(m):
            J[i][j] = (new_f[i] - base[i]) / h

    return J