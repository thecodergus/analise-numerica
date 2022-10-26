using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")


f(x) = sin(x)^3 - 3*sin(x)^2 + sin(x^2) + 4
x0 = 4.4718
x = [4.2499, 4.4024, 4.5379, 4.6815]

printItem(Derivada.derivada_finita(f, x0, x; ordem=2))