using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")


f(x) = x^2 * tan(sin(x / π))
h = 0.32345
x0 = 1.99224
orders = [2, 3, 4, 5, 6]

for i = orders
    printItem(Derivada.extrapolação_Richardson(f, x0, h; ordem = i))
end


