include("AjusteDeCurvas.jl")
include("tool.jl")



c = [1.206, 2.613, 3.0257, 4.4594, 4.7035, 6.0504, 7.2678, 8.3227, 8.4782, 9.7083, 10.7376, 11.8711]
k = [0.6385, 1.8538, 2.0815, 2.8849, 3.0218, 3.2681, 3.5398, 3.7051, 3.7016, 3.8041, 3.847, 3.8739]
values = [1.4246, 3.6235, 6.3261]


(coeffs, f) = AjusteDeCurvas.AjusteDeCurvaHiperbolica(c, k; expoente_x=2)

printVector(coeffs)

for i = values
    printItem(f(i))
end