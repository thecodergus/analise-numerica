import numpy as np
import best_poly as bp

def poly(x, a, b):
    return a * 2 ** (b * x)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':

    x = [0.0045, 0.1008, 0.1452, 0.1931, 0.2371, 0.3317, 0.3509, 0.4247, 0.4555, 0.5016, 0.6032, 0.6248, 0.6783, 0.7744, 0.7828, 0.8369, 0.9222, 0.9673, 1.0342, 1.0961, 1.1122, 1.1941, 1.2532, 1.3256, 1.3777, 1.3966, 1.4652, 1.5297, 1.5568, 1.6348, 1.7074, 1.7233, 1.8179, 1.8439, 1.9236, 1.9656]
    y = [2.3389, 6.0564, 5.896, 5.9324, 6.6932, 7.2159, 7.777, 11.3259, 8.9326, 8.5339, 10.6446, 11.2779, 10.8721, 13.0735, 13.0588, 15.8489, 17.1711, 17.2051, 21.435, 19.9077, 20.2606, 21.6658, 24.5362, 27.3443, 27.5289, 26.9318, 30.6485, 37.1328, 36.3097, 41.0152, 44.959, 45.3594, 51.4399, 55.662, 58.7048, 63.6744]
    y_ = np.log(y)
 
    grau = 1

    a0, a1 =  bp.best_poly(x, y_, grau)

    a = np.exp(a0)
    b = a1/np.log(2)

    print(f'{a = } e {b = }')

    p = build_func(a, b)

    x_values =  [0.3001, 1.2912, 1.6893, 1.8147, 1.9538]

    
    for xi_v in x_values:
        print(p(xi_v))
