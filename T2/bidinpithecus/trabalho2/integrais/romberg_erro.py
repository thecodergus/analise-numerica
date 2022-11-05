from methods import *

'''Use o método de Romberg, com o h indicado, para encontrar uma aproximação 
com erro O(hk) para as integrais a seguir:'''

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)


func = ['math.cos(-x**2/3)', 'math.sqrt(1+x**2)', '(x+1/x)**2', 'math.exp(-x**2)', 'math.exp(x)*math.sin(x)/(1+x**2)']
a = [0.901, 0.112, 0.901, -1.223, 0.226]
b = [1.901, 1.112, 1.901, -0.223, 1.226]
order = [4, 4, 10, 10, 8]
n = [5, 3, 4, 4, 3]


for i in range(len(func)):
    k = int(order[i]/2)
    h = float((b[i]-a[i])/n[i])
    hs = [h/2**i for i in range(k)]
    col1=[trapzRomberg(func[i],a[i],b[i],hi, f) for hi in hs]

    r = romberg(col1)

    print(r,end=", ")
print()