using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")




f(x) = sqrt(sin(cos(log(x^2 + 1) + 2) + 3) + 4)

intervalo = [-1.678, 1.273]
subintervalos = [8, 24, 38, 58, 82, 120, 136, 170, 182, 236, 446]


for i = subintervalos
    printItem(Integral.Regra_de_Simpson(f, intervalo[1], intervalo[2], i))
end