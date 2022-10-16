include("InterpolaçãoPolinomial.jl")
include("tool.jl")




x = [0.4508, 0.8387, 1.9576, 3.2516, 3.672, 4.4219, 5.4025, 5.8523, 6.6802, 8.1581, 8.7294, 9.7709]
y = [4.7754, 4.0845, 3.9656, 3.4797, 3.3698, 3.3161, 3.2902, 3.2091, 3.8706, 4.017, 4.5495, 5.006]
values = [1.5516, 1.7241, 2.8621]



(X, coeffs, Y) = InterpolaçãoPolinomial.regressão_linear(x, y, 2)

f = InterpolaçãoPolinomial.build_polynomial_function(coeffs)

printMatrix(X)
printVector(coeffs)
printVector(Y)

for i = values
    printItem(f(i))
end