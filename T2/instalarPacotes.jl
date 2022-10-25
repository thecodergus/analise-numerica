using Pkg

# https://jverzani.github.io/CalculusWithJuliaNotes.jl/
p = [
    "Polynomials",
    "DifferentialEquations",
    "Symbolics",
    "ForwardDiff",
    "MTH229",
    "TaylorSeries"
]


Pkg.add(join(p, " "))
