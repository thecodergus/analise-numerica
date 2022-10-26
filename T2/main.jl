using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")


f(x) = (x^2) * (ℯ^(-x)) * cos(x) + 1
x0 = 0.9016
x = [0.6797, 0.7037, 0.7276, 0.7558, 0.7864, 0.836, 0.8776, 0.8918, 0.9399, 0.9756, 1.0136, 1.0413, 1.0711, 1.1118, 1.1354]

printItem(Derivada.derivada_finita(f, x0, x; ordem=5))