from itertools import product

def printVector(a):
    for i in a:
        print(f"{i},")

def printMatrix(a):
    h = len(a)

    for i, j in product(range(h), range(h)):
        print(f"{a[i, j]},")