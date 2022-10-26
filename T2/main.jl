using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")


f(x) = 3 * cos((x^2 - 1)^(1 / 3))
x0 = 7.5419
order = 3
x = [7.2982, 7.427, 7.4609, 7.5639, 7.7019, 7.7675]
values = [7.344, 7.5698, 7.7657]

for xp in values
    p = Derivada.taylor_series(f, x0, xp, x; ordem=order)
    printItem(p)
    printItem(abs(f(xp) - p))
end
    