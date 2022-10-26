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
    k = 2 # ordem
    n = 5 # número de pontos

    
    x0 = 4.4718
    x = [4.2499, 4.4024, 4.5379, 4.6815]
    f = lambda x: math.sin(x)**3 - 3*math.sin(x)**2 + math.sin(x**2) + 4

    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    y = [f(xi) for xi in x] 
    print(y)
    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

    # print(f'{coeffs}')
    # print(f'{aprox}')