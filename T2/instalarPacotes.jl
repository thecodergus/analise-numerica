using Pkg

# https://jverzani.github.io/CalculusWithJuliaNotes.jl/
p = [
    "Polynomials",
    "DifferentialEquations"
]


Pkg.add(join(p, " "))