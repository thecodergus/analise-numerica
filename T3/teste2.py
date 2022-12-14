import numpy as np
import math

def aprox(f, f_list, a, b, num_intervals):
    n = len(f_list)
    A = [[0 for _ in range(n)] for _ in range(n)]  #A é simetrica
    B = []
    for i in range(n):
        for j in range(i, n): #elementos na diagonal da matriz 
             def f_ji(x):
                return f_list[j](x) * f_list[i](x)
             
             a_ij = simps(f_ji,a,b,num_intervals) #inetgral de f_j *f_i
             #nao altere mais
             A[i][j] = a_ij
             A[j][i] = a_ij
        def ff_i(x):
            return f(x) * f_list[i](x)
        
        b_i = simps (ff_i,a,b,num_intervals) #inetgral de f *ff_i
        #nao altere mais
        B.append(b_i)
    return np.linalg.solve(A,B)


def build_g(coefs, f_list):
    def func_g(x):
        return sum (ci* fi(x) for ci, fi in zip (coefs, f_list))
    return func_g


def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))



def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')


def romberg(col1):
    n = len(col1)
    col1 = [item for item in col1]

    for j in range(n - 1):     # percorrer as colunas
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):  # percorrer as linhas
            power = j + 1
            temp_col[i] = ((4 ** power) * col1[i + 1] -
                           col1[i]) / (4 ** power - 1)
        col1[:n - 1 - j] = temp_col
    return col1[0]


def trapz(f, a, b, h):
    n = int((b - a)/h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma


def build_func(s, var: str='x'):
    scope = {}
    scope['math'] = math
    func = f'def f({var}): return {s}'
    exec(func, scope)
    return scope['f']


if __name__ == '__main__':

    

    func = lambda x: x**2 * math.cos(x * math.sin(math.log(1 + x**2)))
    funcs = ['2', 'x - 1', 'x**2 + 1', 'x**3 + x - 3', '0.5 * x**4 - 3 * x**2 + 1', 'x**5 - 4 * x + 2', 'x**7-x']
    a = -2.07516
    b = 2.13848

    values = [-1.09376, 0.1173, 0.94834]

    # Configs
    n = 256
    order = 8

    funcs = [*map(build_func, funcs)]  
    
    
    coefs = aprox(func, funcs, a, b, n)
    #essa é a funçao g que melhor se aproxima f(x)
    
    g = build_g(coefs, funcs)
    
    for i in coefs:
        print(f"{i}, ")


    for i in values:
        print(f"{g(i)},")

    def ferro(x):
        return (func(x) - g(x))**2

    
    h = (b-(a))/10
    erro_da_ordem = order // 2
    hs = [h / 2 ** i for i in range(erro_da_ordem)]
    col1 = [trapz(ferro, a, b, hi) for hi in hs]
   
    r = romberg(col1)
    print(r)