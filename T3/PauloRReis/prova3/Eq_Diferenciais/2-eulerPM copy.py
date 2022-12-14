""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.3492 e y0=0.75895. Use o método do ponto médio de Euler com tamanho do passo h=0.1148 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, para k=1,2,…,10. """

import numpy as np

def true_euler(f, x0, y0, h, n):
    for k in range(n):
        y0 += h * f(x0, y0)
        x0 += h        
        print(f'x_{k + 1}={x0} e y_{k+1}={y0}')

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid(f, x0, y0, x_values, n):
    for i in range(n):
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y):
        return y * (2 - x) + x + 1
    
    x0 = 1.51318
    y0 = 1.34282
    x_values = [1.53619, 1.60015, 1.64087, 1.69483, 1.75677, 1.80632, 1.83728, 1.87626, 1.93803, 1.98387, 2.02983, 2.09799, 2.14867, 2.16979, 2.25202, 2.29593, 2.33912, 2.36925, 2.4355, 2.49306]
    n = 20
    
    
    r2 = euler_mid(f, x0, y0, x_values, n) #euler ponto medio
    for _, i in r2:
        print(f"{i},")