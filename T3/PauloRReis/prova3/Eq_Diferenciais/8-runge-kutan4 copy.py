""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.466 e y0=2.389. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.107. """

def RK4(f, x0, y0, x_values, n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    return y*(1-x)+x+2
    
if __name__ == "__main__":    
    func = lambda x,y: y * (1 - x) + x + 2
    x0 = 0.4727
    y0 = 0.8166
    x_values = [0.4792, 0.5625, 0.5871, 0.6594, 0.6861, 0.7451, 0.7889, 0.8394, 0.9011, 0.9562, 1.0007, 1.0676, 1.1058, 1.154, 1.2097, 1.2378, 1.2939, 1.3639, 1.4173, 1.4374]
    
    n = 20
    
    r = RK4(func,x0,y0, x_values,n)
    
    for _, i in r:
        print(f"{i},")
