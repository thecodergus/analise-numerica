from methods import *

'''
A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 segundos, numa corrida na Daytona International Speedway, Flórida.
'''

answer = []
x = []
y = []


lista = [
    [0.0,   155.99],
    [5.0,   295.91],
    [10.0,	122.25],
    [15.0, 	171.04],
    [20.0, 	282.65],
    [25.0, 	264.57],
    [30.0, 	197.16],
    [35.0, 	142.17],
    [40.0, 	248.36],
    [45.0, 	230.09],
    [50.0, 	185.28],
    [55.0, 	211.49],
    [60.0, 	108.22]
]

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
