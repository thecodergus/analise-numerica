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
    c = 0.289
    r = 1.4473
    l = 1.8267

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0619*pi*t) => e_value = 0.0619
    e_value = 0.0543

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.0715
    n = 150
    b = 1/2
    x_values = [0.055, 0.1829, 0.2648, 0.3106, 0.4517, 0.5785, 0.6316, 0.7271, 0.8143, 0.97, 1.0869, 1.1283, 1.2486, 1.3862, 1.4149, 1.5686, 1.6158, 1.7561, 1.8392, 1.9759, 2.0306, 2.1669, 2.2147, 2.3838, 2.4776, 2.5402, 2.6631, 2.7701, 2.8108, 2.9498, 3.0891, 3.1196, 3.2867, 3.3135, 3.464, 3.5323, 3.6229, 3.7559, 3.8552, 3.9353, 4.0639, 4.1563, 4.282, 4.3407, 4.4113, 4.5861, 4.6494, 4.7616, 4.8428, 4.9461, 5.0835, 5.1719, 5.2448, 5.3682, 5.4292, 5.5444, 5.652, 5.7723, 5.8589, 5.9377, 6.0199, 6.1173, 6.2135, 6.3108, 6.417, 6.5213, 6.6524, 6.7584, 6.8538, 6.9739, 7.0476, 7.1159, 7.2695, 7.3258, 7.4163, 7.5765, 7.6419, 7.7687, 7.8858, 7.9772, 8.012, 8.1873, 8.2383, 8.3222, 8.4174, 8.5878, 8.6351, 8.7261, 8.8547, 8.917, 9.0217, 9.1488, 9.2142, 9.3199, 9.4319, 9.5633, 9.6538, 9.7394, 9.8266, 9.9545, 10.0412, 10.1597, 10.2377, 10.3702, 10.4175, 10.5307, 10.6813, 10.7782, 10.8321, 10.92, 11.0744, 11.1592, 11.266, 11.3824, 11.4213, 11.5805, 11.6629, 11.7359, 11.8479, 11.9342, 12.0713, 12.1847, 12.2561, 12.3141, 12.4572, 12.5796, 12.6285, 12.775, 12.8685, 12.9477, 13.054, 13.1522, 13.2162, 13.3899, 13.4561, 13.5557, 13.6562, 13.7258, 13.8584, 13.9684, 14.014, 14.126, 14.2475, 14.3169, 14.4342, 14.518, 14.6614, 14.7484, 14.8389, 14.9334]

    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2_h_variavel(g, x0, y0, n, b, x_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

    plt.scatter(lista_x, lista_y)

    plt.savefig('edo.png')