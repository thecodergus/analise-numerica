# import math
from numpy import *
# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


f = lambda x: sin(e**(-x**2)) + 1
a, b = [-1.68, 1.752]
subintervalos = [1, 11, 31, 74, 76, 147, 172, 381, 605, 790, 2863, 6030]

for i in range(len(subintervalos)):
    r = trapz(f, a, b, subintervalos[i])
    print(r)