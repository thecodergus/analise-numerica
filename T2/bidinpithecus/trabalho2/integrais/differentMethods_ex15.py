from methods import *

'''
Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à medida que o tempo passa, conforme mostrado na tabela a seguir.
'''

answer = []
x = []
y = []

lista = [
    [0.0, 9.86],
    [0.75, 9.33],
    [1.5, 8.95],
    [2.25,8.45],
    [3.0,8.16],
    [3.75,7.83],
    [4.5,7.23],
    [5.25,6.98],
    [6.0,6.58],
    [6.75,	6.2],
    [7.5,5.54],
    [8.25,5.31],
    [9.0,4.89],
    [9.75,4.39],
    [10.5,3.98],
    [11.25,3.56],
    [12.0,3.09]
]


for i in range(len(lista)):
    x.append(lista[i][0])
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
