import numpy as np
from numpy.linalg import solve
from numpy import zeros, double, array
from sympy.abc import x
from sympy import lambdify
import sympy as math
from itertools import *
from print import *

class CombinacaoLinear:
    def __init__(self, f, fs, a, b):
        self.f = lambdify([x], f)
        self.funcs = [*map(lambda a: lambdify([x], eval(a)), fs)]
        self.a = a
        self.b = b

    def trapezio(self, f, a, b, h):
        n = (b - a) // h
        soma = sum(map(lambda i: f(a) + i * h, range(1, n))) * 2

        return (h / 2) * (f(a) + f(b) + soma)
        

    def romberg(self, col1):
        n = len(col1)
        col1 = array(col1)

        for j in range(n - 1):     # percorrer as colunas
            temp_col = zeros(n - 1 - j)
            for i in range(n - 1 - j):  # percorrer as linhas
                power = j + 1
                temp_col[i] = ((4 ** power) * col1[i + 1] - col1[i]) / (4 ** power - 1)
            col1[:n - 1 - j] = temp_col
        return col1[0]

    # Aprox
    def get_coefs(self, n = 256):
        k = len(self.funcs)
        A = zeros((k, k), dtype=double)
        B = zeros(k, dtype=double)

        for i, j in product(range(k), range(k)):
            if j >= i:
                A[i, j] = self.trapezio(lambda a: self.funcs[j](a) * self.funcs[i](a), self.a, self.b, n)
            else:
                A[i, j] = A[j, i]

            B[i] = self.trapezio(lambda a: self.f(a) * self.funcs[i](a), self.a, self.b, n)


        return solve(A, B)

    def best_func(self, n = 256):
        return lambda x: sum(map(lambda a, f: f(x) * a, self.get_coefs(n=n), self.funcs))
    
    def quadratura(f, pontos, pesos):
        return sum(map(lambda a, b: f(a) * b, pontos, pesos))

    def change(f, a, b):
        return lambda x: f((b + a) / 2 + (b - a) * x / 2) * (b - a) / 2

    def erro(self, ordem = 512):
        h = (self.b - self.a) / 10
        hs = [h / 2 ** i for i in range(ordem // 2)]
        # f = lambda x: ( - )

        # col1 = [*map(lambda x: self.trapezio(, self.a, self.b, x), hs)]

        return self.romberg(col1)

if __name__ == "__main__":
    func = x**2 * math.exp(x) * math.sqrt(math.log(2 + math.cos(-x**2)))
    funcs = ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5', 'x**6', 'x**7', 'x**8']
    a = -2.1461
    b = 0.8646

    values = [
        -1.62697,
        -0.95364,
        0.1389
    ]


    problema = CombinacaoLinear(func, funcs, a, b)
    coefs = problema.get_coefs(n=256)
    f = problema.best_func(n=256)

    printVector(coefs)
    printVector(map(lambda x: f(x), values))

    # printItem(problema.calc_erro(values, n=512))