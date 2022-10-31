module Integral
    function Regra_do_Trapezio(f::Function, variavel_inferior::Float64, variavel_superior::Float64, intervalos::Int64)::Float64
        h::Float64 = (variavel_superior - variavel_inferior) / intervalos

        return ((sum(f.(variavel_inferior .+ (collect(1:(intervalos - 1)) .* h))) * 2) + (f(variavel_inferior) + f(variavel_superior))) * (h/2)
    end

    function Regra_do_Trapezio_Ponto(x::Vector{Float64}, y::Vector{Float64})::Float64
        return sum([((x[i + 1] - x[i])/2) * (y[i] + y[i + 1]) for i = 1:(length(x) - 1)])
    end

    function Regra_de_Simpson(f::Function, variavel_inferior::Float64, variavel_superior::Float64, intervalos::Int64)::Float64
        h::Float64 = (variavel_superior - variavel_inferior) / intervalos

        return (h/3) * (f(variavel_inferior) + 4 * sum(f.((collect(1:2:(intervalos - 1)) .* h) .+ variavel_inferior)) + 2 * sum(f.((collect(2:2:(intervalos - 1)) .* h) .+ variavel_inferior)) + f(variavel_superior))
    end

    function Regra_de_Simpson_Ponto(x::Vector{Float64}, y::Vector{Float64})::Float64
        regra_de_simpson(x0, x1, y0, y1, y2) = ((x1-x0)/3)*(y0+4*y1+y2)
        
        return sum([regra_de_simpson(x[k],x[k+1],y[k],y[k+1],y[k+2]) for k = 1:2:(length(x) - 1)])
    end
end