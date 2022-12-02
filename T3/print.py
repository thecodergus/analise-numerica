from itertools import product

def printVector(a):
    for i in a:
        print("{:.7f},".format(i))

def printMatrix(a):
    h = len(a)

    for i, j in product(range(h), range(h)):
        print("{:.7f},".format(a[i, j]))

def printItem(x):
    print("{:.7f},".format(x))