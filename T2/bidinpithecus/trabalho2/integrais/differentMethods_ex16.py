from methods import *

'''
Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) em direção à ISS (International Space Station) com a missão de levar o AMS-2 (Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.
'''

answer = []
x = []
y = []

lista = [
    [0, 	0],
    [5, 	110],
    [10, 	232],
    [15 ,	363],
    [20 ,	514],
    [25 ,	676],
    [30 ,	817],
    [35 ,	966],
    [40 ,	1085],
    [45 ,	1209],
    [50 ,	1318],
    [55 ,	1461],
    [60 ,	1637],
    [65 ,	1827],
    [70 ,	2054],
    [75 ,	2315],
    [80 ,	2603],
    [85 ,	2902],
    [90 ,	3204]
]

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
