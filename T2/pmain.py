import numpy as np

'''
Um pesquisador relatou os dados tabulados a seguir....
sqrt( y ) = 1/b + a/b * 1/sqrt( x )

'''

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp


def modelo(x):
    a, b = -10, 10
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x - 1.86 * x ** 2 - 3.21 * x ** 3 + erro


if __name__ == '__main__':
    

    
    x = [0.5667, 1.5096, 2.3408, 3.5973, 4.3679, 4.7608, 5.6185, 6.5097, 7.5643, 7.7321, 8.6808, 9.9977]
    y = [4.6522, 2.2459, 1.5706, 1.2947, 1.1762, 0.9487, 0.9418, 0.9899, 0.7272, 0.7126, 0.7668, 0.678]
    values = [6.4653, 7.6653, 9.0401]


    y_ = np.sqrt(y)
    
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)

    n = len(coefs)

    for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'y(x{xi+1}) = {(a0 + a1 * 1/np.sqrt(values[xi]))**2}')