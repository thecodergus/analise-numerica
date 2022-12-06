import numpy as np
math = np





if __name__ == "__main__":

    func = x**2 * math.exp(x) * math.sqrt(math.log(2 + math.cos(-x**2)))
    funcs = ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5', 'x**6', 'x**7', 'x**8']
    a = -2.12319
    b = 0.80603

    values = [
    -1.40511, -0.83783, 0.67539 
    ]

    funcs = [*map(lambda x: eval(x), funcs)]