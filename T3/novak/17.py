import math
from re import A
import numpy as np
from cachetools import cached, LRUCache, TTLCache



def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def simps(f, a, b, n):
    if n % 2 != 0:
        print('O valor n deve ser par')
        return None

    num_parabolas = n / 2
    soma = 0
    h = (b - a) / n

    for i in range(int(num_parabolas)):
        x0 = a + (2 * i) * h
        x1 = a + (2 * i + 1) * h
        x2 = a + (2 * i + 2) * h
        soma += f(x0) + 4 * f(x1) + f(x2)

    soma *= h / 3

    return soma


def coef(f,g):
    # a = -1.05973 
    # b=1.4086
    a=-1.07173
    b=1.45137
    n = 500 
    func = lambda x: (f(x) * g(x) ) 
    func2 = lambda x: g(x) * g(x)
    numer = simps(func,a,b,n)
    denom = simps(func2,a,b,n)
    
    return (numer/denom)




# def coefs_comb(f, funcs):
#     a = -1
#     b= 1
#     n = 256
#     list_coefs = []
#     for gk in funcs:
#         numer = trapz(
#             lambda x: f(x) * gk(x),
#             a,
#             b,
#             n
#             )
#         denom = trapz(
#             lambda x: gk(x) * gk(x),
#             a,
#             b,
#             n
#                     )
#         ck = numer/denom
#         list_coefs.append(ck)
#     return list_coefs
        
# fs = [lambda x: x**i for i in range(10)]
fs = [
    lambda x: x**0,
    lambda x: x**1,
    lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4,
    lambda x: x**5,
    lambda x: x**6,
    lambda x: x**7,
    lambda x: x**8,
    lambda x: x**9,
]

def f(num):
    # print(f"f - {num}")
    if num == 1:
        return lambda x: 1
    return fs[num - 1]

def g(num):
    if num == 1:
        return lambda x: f(num)(x)

    # print(f"g - {num}")
    return lambda x: f(num)(x) - sum([a(num, i) * g(i)(x) for i in range(1, num)])

@cached(cache={})
def a(a, b):
    return coef(f(a), g(b))

if __name__ == '__main__':
    question = [[(a, b) for b in range(1, a)] for a in range(2, 11)]

    for linha in question:
        for a1, b1 in linha:
            print(f"{a(a1, b1)},", end="")
    
    
        
        