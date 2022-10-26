import numpy as np
import math

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matrz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    return np.linalg.solve(A, B)

def dif_fin(coeffs, y):
    # print([ci * yi for ci, yi in zip(coeffs, y)])
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    ordem = 5 # ordem

    
    x0 = 1.5061
    x = [1.2623, 1.3102, 1.356, 1.3724, 1.4005, 1.4316, 1.4651, 1.5162, 1.5521, 1.5807, 1.6022, 1.6304, 1.6734, 1.7104, 1.7534]
    f = lambda x: x**2 * math.exp(-x) * math.cos(x) + 1
    n = len(x)

    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    y = [f(xi) for xi in x] 
    coeffs = coeffs_dif_fin(x0, x, ordem)
    aprox = dif_fin(coeffs, y)

    # print(f'{coeffs}')
    print(f'{aprox}')