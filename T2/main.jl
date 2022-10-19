include("InterpolaçãoPolinomial.jl")
include("tool.jl")


x = [1.5115, 3.4958, 5.0553, 6.1924, 8.5711, 9.2044, 12.0713, 13.6181, 14.876, 16.5502, 17.4019, 19.4549]
y = [2.1715, 2.9808, 3.3037, 3.4466, 3.6233, 3.6503, 3.7521, 3.7947, 3.8544, 3.8293, 3.9087, 3.9145]
values = [4.7458, 9.9365, 13.9922]


(coeffs, f) = InterpolaçãoPolinomial.AjusteDeCurvaHiperbolica(x, y, 1)
# coeffs = InterpolaçãoPolinomial.AjusteDeCurvaHiperbolica(x, y, 1)
# f = InterpolaçãoPolinomial.build_polynomial_function(coeffs)


# # printMatrix(X)
printVector(coeffs)
# # printVector(Y)
# # print(f)

for i = values
    printItem(f(i))
end