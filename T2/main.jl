include("AjusteDeCurvas.jl")
include("tool.jl")




c = [1.2605, 2.3431, 3.4354, 4.2371, 5.0377, 6.0567, 7.355, 7.8037, 9.2344, 9.9905, 10.2755, 11.3764]
k = [0.5925, 1.4691, 2.0282, 2.2095, 2.4951, 2.6579, 2.8092, 2.8185, 2.9939, 2.9636, 3.1621, 2.8669]
values = [2.1815, 4.874, 8.2284]




(coeffs, f) = AjusteDeCurvas.AjusteDeCurvaHiperbolica(c, k)

printVector(coeffs)

for i = values
    printItem(f(i))
end