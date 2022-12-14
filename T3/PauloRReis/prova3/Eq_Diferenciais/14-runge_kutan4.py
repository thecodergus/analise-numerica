"""No livro Looking at History Through Mathematics, Rashevsky [Ra], p. 103-110, considera um modelo para um 
problema envolvendo a produção de rebendes na sociedade. Considere uma sociedade com x(t) indivíduos no 
instante t, em anos, e suponha que todo rebelde que se acasale com outro rebelde tenha filhos também rebeldes, 
enquanto uma proporção fixa r de todos os filhos de outros tipos de acasalamento também seja rebelde. Se for 
suposto que as taxas de nascimento e mortalidade para todos os indivíduos são as constantes λ e μ, 
respectivamente, e se não rebeldes e rebeldes se acasalam aleatoriamente, o problema pode ser expresso pelas 
equações diferenciais
dx(t)dt=(λ−μ)x(t)edxn(t)dt=(λ−μ)xn(t)+rλ(x(t)−xn(t)),
em que xn(t) denota o número de rebeldes na população no instante t.
Suponha que a variável p(t)=xn(t)/x(t) seja introduzida para representar a proporção de rebeldes na sociedade 
no instante t. Neste caso, as equações diferenciais acima podem ser combinadas e simplificadas na única 
equação diferencial
dp(t)dt=rλ(1−p(t)).
Considerando p(t0)=p0, com t0=0, p0=0.00159, λ=0.01046, μ=0.006 e r=0.11114, use o método de Runge-Kutta de 
ordem 4 para encontrar aproximações para a solução p(t) nos instantes
Além disso, encontre a solução algébrica exata p(t) e calcule os erros |p(tk)−pk|, k=1,2,…,150. Por fim,
reflita sobre o que acontecerá com a taxa de rebeldes nessa sociedade depois de alguns séculos."""

import numpy
math = numpy

def RK4(f, x0, y0, val, n):
    for i in range(n):
        if i==0:
            h=val[i]-x0
        else:
            h=val[i]-val[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        m3 = f(x0 + (h/2), y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        yield[x0, y0]
    

# r = 0.15088
# lambd = 0.02561

# modificar valores de r e lambd    
def f(p, t):
    r = 0.19293
    lambd = 0.01405
    k = r * lambd
    return k * (1 - t)


# solução exata:
# modificar valores de r, lambd e coef 
def p(t):
    r = 0.19293
    lambd = 0.01405
    k = r * lambd
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao
    coef = 0.99885
    return 1 - (coef * math.exp(-k*t))
    


if __name__ == "__main__":
    # modificar valor de p0
    t0 = 0
    p0 = 0.00115
    n = 150
    t_values = [0.44639, 1.18435, 1.80917, 2.13682, 3.25586, 3.87851, 4.34735, 4.80749, 5.82051, 6.26953, 6.96412, 7.65203, 8.35267, 9.0635, 9.74376, 10.26743, 10.9923, 11.61853, 12.39349, 13.02951, 13.77127, 14.13431, 14.98692, 15.81052, 16.42499, 17.25055, 17.87265, 18.48229, 19.03501, 19.51496, 20.40744, 20.75526, 21.44147, 22.25376, 22.79594, 23.71188, 24.09289, 24.97662, 25.44189, 26.23622, 26.7783, 27.49079, 28.48601, 29.05654, 29.6517, 30.50705, 31.21155, 31.62522, 32.58748, 33.12559, 33.42819, 34.341, 34.83664, 35.69016, 36.47288, 36.776, 37.84705, 38.19208, 39.02441, 39.80344, 40.46047, 40.85973, 41.77652, 42.35066, 42.89306, 43.89263, 44.11958, 44.87039, 45.9291, 46.1422, 47.22931, 47.62383, 48.53888, 49.01938, 49.85299,
                50.3527, 51.09282, 51.43343, 52.44709, 53.08216, 53.76888, 54.47084, 55.26051, 55.86608, 56.53928, 57.09738, 57.78912, 58.43272, 58.89414, 59.92123, 60.28078, 60.74174, 61.81414, 62.48074, 63.13066, 63.79097, 64.50421, 64.81833, 65.52091, 66.43101, 67.19501, 67.90065, 68.54728, 68.88685, 69.87057, 70.45907, 71.21123, 71.50569, 72.16973, 72.91961, 73.45471, 74.49099, 75.00874, 75.7791, 76.2072, 77.21988, 77.43372, 78.44048, 79.1538, 79.92114, 80.34052, 81.05022, 81.76062, 82.39377, 83.04893, 83.41219, 84.27747, 85.1931, 85.93088, 86.58523, 87.05885, 87.46708, 88.22593, 89.0259, 89.40455, 90.4071, 90.84678, 91.53797, 92.29215, 92.93703, 93.58997, 94.57365, 94.80411, 95.71324, 96.57759, 96.90194, 97.60477, 98.25828, 98.95633, 99.86683]

    r = RK4(f, t0, p0, t_values, n)

    runge = [*map(lambda a: a[1], r)]

    for i in range(n):
        print(f"{runge[i]}, {abs(p(i) - runge[i])},", end="")
