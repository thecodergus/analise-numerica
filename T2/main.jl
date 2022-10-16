include("InterpolaçãoPolinomial.jl")
include("tool.jl")



x = [0.0881, 0.2199, 0.3709, 0.552, 0.713, 0.8487, 1.1358, 1.2648, 1.4314, 1.6439, 1.7936, 1.8714]
y = [6.9983, 7.6152, 8.1006, 11.0015, 13.9742, 16.5418, 27.3878, 32.7363, 41.555, 59.1029, 73.3571, 83.2471]
values = [1.3774, 1.5064, 1.5594]



(X, coeffs, Y) = InterpolaçãoPolinomial.regressão_linear(x, y, 1)

f = InterpolaçãoPolinomial.build_polynomial_function(coeffs)

# printMatrix(X)
printVector(coeffs)
# printVector(Y)

for i = values
    printItem(f(i))
end