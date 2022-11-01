using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")



approximations = [0.19218318267904433, 0.15847702334348135, 0.1405666594774786, 0.13139416993708863, 0.12675930873813002, 0.12443042671972648]

printItem(Derivada.extrapolação_Richardson(approximations))