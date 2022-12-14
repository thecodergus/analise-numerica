""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.967 e y0=2.757. Use o método de Heun para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.196. """

def heun(f,x0,y0,x_values,n):
    r = []
    for i in range(n):
        m1 = f(x0,y0)
        if i > 0:
            h = x_values[i] - x_values[i - 1]
        else:
            h = x_values[i] - x0
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h *(m1 + m2) / 2
        x0 += h
        y0 = y1
        r.append((x0,y0))
    return r

def f(x,y):
    return y*(2-x)+x+1

if __name__ == "__main__":    
    
    func = lambda x, y: y * (2 - x) + x + 1
    x0 = 1.83133
    y0 = 0.85992
    x_values = [1.86817, 1.88815, 1.94545, 2.02543, 2.05031, 2.10582, 2.15358, 2.18977, 2.2544, 2.32432, 2.37089, 2.39414, 2.46812, 2.52294, 2.55626, 2.59318, 2.64786, 2.72238, 2.76302, 2.81173]
    n = 20

    
    r = heun(func, x0, y0, x_values, n)

    for _, v in r:
        print(f"{v},")
