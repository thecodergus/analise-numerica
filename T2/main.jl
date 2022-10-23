using Test

include("AjusteDeCurvas.jl")
include("tool.jl")


x = [0.6924, 1.4605, 2.7377, 3.4508, 4.186, 5.1095, 5.2956, 6.1019, 7.0271, 7.8615, 9.1405, 9.2407]
y = [5.4553, 3.0073, 1.962, 1.636, 1.4647, 1.3665, 1.2926, 1.2741, 1.145, 1.0142, 0.979, 0.9006]
values = [3.2064, 3.2717, 7.0076]


(coeffs, f) = AjusteDeCurvas.AjusteDeCurva3(x, y)

printVector(coeffs)

# @test round.(coeffs, digits=7) == round.([3.30504266097, 2.13763041463], digits=7)
# @test round.(f.(values), digits=7) == round.([1.77223866524, 1.74925576, 1.10643229204], digits=7)

for i = values
    printItem(f(i))
end