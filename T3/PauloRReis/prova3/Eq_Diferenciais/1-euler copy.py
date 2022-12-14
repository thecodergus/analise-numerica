""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.223 e y0=1.14. Use o método de Euler com tamanho do passo h=0.125 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, para k=1,2,…,10. """

import math
import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, h, n):
    result = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
    return result

def euler_mod(f, x0, y0, x_values, n):
    result = []
    for i in range(n):
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        y0 += f(x0, y0) * h
        x0 += h
        result.append([x0, y0])
    return result

if __name__ == '__main__':

    def f(x, y):
        return y * (1 - x) + x + 2

    x0 = 1.59227
    y0 = 0.46106
    x_values = [1.6179, 1.67767, 1.73377, 1.75399, 1.83367, 1.85471, 1.93409, 1.95368, 2.01748, 2.07944, 2.13287, 2.16504, 2.20134, 2.28575, 2.30813, 2.37466, 2.43622, 2.4615, 2.53193, 2.5481]
    n = 20

    #P3.7
    # def f(x, y):
    #     return y*(1 - x) + x + 2

    # x0, y0 = 1.47205, 2.16382
    # h = 0.13102
    # n = 10

    # resposta = euler(f, x0, y0, h, n)
    resposta = euler_mod(f, x0, y0, x_values, n)
    
    for _, i in resposta:
        print(f"{i},")

    def y(x):
        return 5 * math.exp(x - 1) - x - 2

    ##Visualizacao
""" t = np.linspace(x0, x0 + n * h, 100)
    yt = [y(i) for i in t]

    cx, cy = zip(*resposta)

    plt.plot(t, yt)
    plt.scatter(cx, cy)
    plt.savefig('euler.png') """