""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.776 e y0=0.981. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.131. """

def ralston(f, x0, y0, x_values, n):
    for i in range(n):
        m1 = f(x0, y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0 + 3/4 * h, y0 + m1 *3/4 * h )
        y0 += h * (m1 + 2 * m2) / 3
        x0 += h
        yield [x0,y0]

def f(x,y):
    return y*(2-x)+x+1


    
    
    
if __name__ == "__main__":
    func = lambda x, y: y * (2 - x) + x + 1
    
    x0 = 1.88655
    y0 = 2.467
    x_values = [1.90995, 1.96422, 2.02473, 2.06274, 2.11045, 2.18018, 2.21336, 2.2683, 2.31634, 2.36422, 2.4231, 2.473, 2.50741, 2.57028, 2.59579, 2.66386, 2.70827, 2.7744, 2.80534, 2.87403]
    
    n = 20


    e = ralston(f,x0,y0, x_values, n)
    
    for _, i in e:
        print(f"{i},")