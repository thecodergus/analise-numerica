using Pkg

# https://jverzani.github.io/CalculusWithJuliaNotes.jl/
pacotes = [
    "Polynomials",
    "DifferentialEquations",
    "Symbolics",
    "ForwardDiff",
    #"MTH229",
    "TaylorSeries"
]

Pkg.add(pacotes)

