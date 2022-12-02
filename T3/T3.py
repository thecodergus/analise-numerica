import numpy as np
from numpy import array, zeros, double
from sympy.abc import x
from sympy import lambdify
import math
from itertools import *

class CombinacaoLinear:
    def __init__(self, f, fs, a, b):
        self.func = lambdify([x], f)
        self.funcs = [*map(lambda a: lambdify([x], eval(a)), fs)]
        self.a = a
        self.b = b

    def trapezio(self, f, a, b, n = 256):
        h = abs(b - a) / n
        sum_fx = sum(map(lambda i: f(a + i * h), range(1, n))) * 2

        return (f(a) + sum_fx + f(b)) * (h / 2)

    def best_func(self, n = 256):
        k = len(self.funcs)
        A = zeros((k, k), dtype=double)
        B = zeros(k, dtype=double)

        for i, j in product(range(k), range(k)):
            if j >= i:
                A[i, j] = self.trapezio(lambda a: self.funcs[j](a) * self.funcs[i](x), self.a, self.b, n)
            else:
                A[i, j] = A[j, i]

            B[i] = self.trapezio(lambda a: self.f(a) * self.funcs[i](a), self.a, self.b, n)

    def quadratura(f, pontos, pesos):
        return sum(map(lambda a, b: f(a) * b, pontos, pesos))

    def change(f, a, b):
        return lambda x: f((b + a) / 2 + (b - a) * x / 2) * (b - a) / 2


if __name__ == "__main__":
    pass