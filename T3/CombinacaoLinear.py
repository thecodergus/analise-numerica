import numpy as np
from numpy.linalg import solve
from numpy import zeros, double
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

    def trapezio(self, f, a, b, n = 256):
        h = abs(b - a) / n
        sum_fx = sum(map(lambda i: f(a + i * h), range(1, n))) * 2

        return (f(a) + sum_fx + f(b)) * (h / 2)

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


    def erro(self, x, n = 512):
        return (self.f(x) - self.best_func(n=n))**2

if __name__ == "__main__":
    func = 2 * math.sin(x) + math.cos(-x**2)
    funcs = ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5']
    a = -0.81969
    b = 2.30316

    values = [
        -0.28189,
        0.6078,
        1.87729
    ]


    problema = CombinacaoLinear(func, funcs, a, b)
    coefs = problema.get_coefs(n=256)
    f = problema.best_func(n=256)

    printVector(coefs)
    printVector([*map(lambda x: f(x), values)])

    # print(problema.erro(n=512))