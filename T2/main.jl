include("InterpolaçãoPolinomial.jl")
include("tool.jl")






x = [1.454, 2.71, 5.4475, 5.9073, 7.9261, 9.9695, 11.9958, 12.1671, 14.6046, 16.1558, 18.2149, 19.5855]
y = [2.3399, 2.9291, 3.3685, 3.4383, 3.5481, 3.6839, 3.7044, 3.6355, 3.6948, 3.7906, 3.8051, 3.8312]
values = [5.5459, 15.9459, 17.6236]



# (coeffs, f) = InterpolaçãoPolinomial.AjusteDeCurvaGeométrica(x, y, 1)
coeffs = InterpolaçãoPolinomial.AjusteDeCurvaHiperbolica(x, y, 1)
f = InterpolaçãoPolinomial.build_polynomial_function(coeffs)


# printMatrix(X)
printVector(coeffs)
# printVector(Y)
# print(f)

# for i = values
#     printItem(f(i))
# end