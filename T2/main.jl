include("InterpolacaoPolinomial.jl")
include("tool.jl")



x = [0.0109, 0.8969, 1.7801, 2.8683, 4.004, 4.2499, 5.0442, 6.4043, 6.7618, 8.1742, 9.0051, 9.9303]
y = [0.6838, 2.224, 3.959, 5.8476, 8.1818, 8.7214, 10.3173, 12.9015, 13.4349, 16.2593, 17.4278, 18.8074]
values = [2.3136, 6.7516, 9.446]


printVector(InterpolacaoPolinomial.vanderMonde(x, y, 2))
f = InterpolacaoPolinomial.build_polynomial_function(x, y, 2)
for i = values
    printLine(f(i))
end