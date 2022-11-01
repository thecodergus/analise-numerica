import numpy as np
import matplotlib.pyplot as plt


def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return -y/np.sqrt(9**2-y**2)


def g(t, i):
    c = 0.2761
    r = 1.4153 
    l = 1.767

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0741

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.0511
    n = 150
    b = 2/3
    x_values = [0.0216, 0.1726, 0.2692, 0.3495, 0.4293, 0.5539, 0.665, 0.7536, 0.8493, 0.9721, 1.0713, 1.1136, 1.2238, 1.3475, 1.4614, 1.5571, 1.6688, 1.7402, 1.831, 1.9427, 2.0514, 2.1304, 2.236, 2.379, 2.4536, 2.5732, 2.6677, 2.727, 2.836, 2.9557, 3.0676, 3.1711, 3.2303, 3.3255, 3.4353, 3.5426, 3.6474, 3.7612, 3.8463, 3.9451, 4.0137, 4.1233, 4.2258, 4.3804, 4.4593, 4.5383, 4.6669, 4.7266, 4.8353, 4.972, 5.0887, 5.144, 5.2827, 5.3484, 5.4777, 5.5883, 5.6206, 5.7755, 5.8515, 5.9778, 6.0745, 6.1314, 6.2543, 6.3556, 6.4465, 6.5103, 6.6453, 6.7126, 6.8108, 6.939, 7.0146, 7.1371, 7.2406, 7.3136, 7.4664, 7.5128, 7.6876, 7.7618, 7.8851, 7.9104, 8.08, 8.1645, 8.2311, 8.3594, 8.4326, 8.5205, 8.6455, 8.7567, 8.8367, 8.9727, 9.0514, 9.1169, 9.2447, 9.3801, 9.485, 9.5735, 9.6742, 9.7763, 9.8251, 9.9872, 10.0778, 10.1321, 10.2844, 10.3335, 10.4799, 10.5701, 10.6847, 10.722, 10.8424, 10.9473, 11.0248, 11.1853, 11.2718, 11.3811, 11.4497, 11.5857, 11.6399, 11.7516, 11.8867, 11.9436, 12.0741, 12.1307, 12.2829, 12.3564, 12.4387, 12.5103, 12.6356, 12.7701, 12.845, 12.956, 13.0605, 13.1261, 13.2819, 13.3126, 13.4277, 13.585, 13.658, 13.7683, 13.826, 13.9217, 14.0144, 14.1145, 14.2835, 14.3412, 14.4854, 14.5683, 14.653, 14.7695, 14.8301, 14.9877]

    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2(g, x0, y0, h, n, b)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')