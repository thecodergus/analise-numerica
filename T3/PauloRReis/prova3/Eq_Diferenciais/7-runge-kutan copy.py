""" Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.053 e y0=1.787. Use o método de Runge-Kutta de ordem 2 com b=0.53 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.175. """

def RK2(f, x0, y0, h, n, b=0.53):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y*(1-x)+x+2
    
if __name__ == "__main__":
    func = lambda x, y: y * (1 - x) + x + 2
    
    x0 = 0.32927
    y0 = 0.72252
    x_values = [0.37286, 0.40883, 0.45377, 0.50287, 0.55595, 0.58938, 0.65525, 0.6953, 0.76246, 0.80599, 0.85746, 0.88519, 0.96577, 0.99021, 1.05755, 1.11732, 1.13588, 1.2115, 1.2726, 1.30511]
    b = 0.82357

    n = 20
    
    e = RK2(f,x0,y0, x_values,n, b)

    for _, i in e:
        print(f"{i},")