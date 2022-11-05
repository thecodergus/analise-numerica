from methods import *

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)

def change(nome_funcao, a, b):
    def g(u):
        return f(nome_funcao, (b+a)/2 + (b-a)*u/2) * (b-a)/2
    return g


funcs = ['math.cos(-x**2/3)', 'math.exp(-x**2)', '(x+1/x)**2', 'math.exp(x)*math.sin(x)/(1+x**2)', 'math.log(math.sqrt(1+x**2))']
a = [-1.863, -1.047, 0.86, 0.932, 1.395]
b = [1.387, 1.1, 2.451, 2.322, 3.628]
exact_for_degree_less_than = [6, 4, 10, 12, 8]


for i in range(len(funcs)):
    order = str(int(exact_for_degree_less_than[i]/2))
    txt_order = ['raiz'+order, 'peso'+order]
    r = quadratura(change(funcs[i], a[i], b[i]), locals()[txt_order[0]], locals()[txt_order[1]])
    print(r, end=", ")
print()