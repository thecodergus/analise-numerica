using Test

include("modules/AjusteDeCurvas.jl")
include("modules/Derivada.jl")
include("modules/Integral.jl")
include("tools/prints.jl")



approximations = [0.3218931348145695, 0.3075624680704223, 0.29890438649758266, 0.29423147087288726, 0.2918126941260937, 0.2905831808048447]
printItem(Derivada.extrapolação_Richardson(approximations))