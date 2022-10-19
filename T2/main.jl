include("InterpolaçãoPolinomial.jl")
include("tool.jl")




x = [0.6406, 1.2475, 2.0579, 3.1441, 3.5033, 4.7584, 5.6428, 6.5909, 7.002, 8.2274, 8.5666, 9.9025]
y = [2.1128, 3.1782, 3.7176, 3.7828, 3.5228, 2.793, 2.2604, 1.8121, 1.5919, 1.1522, 1.0173, 0.7811]
values = [3.313, 3.9927, 5.2419]




(coeffs, f) = InterpolaçãoPolinomial.AjusteDeCurvaExponencial2(x, y)

printVector(coeffs)

for i = values
    printItem(f(i))
end