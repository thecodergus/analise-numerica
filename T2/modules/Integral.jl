module Integral
    function Regra_do_Trapezio(f::Function, variavel_inferior::Float64, variavel_superior::Float64, intervalos::Float64)::Float64
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

    function trapzcomp(f::Function, a::Float64, b::Float64, n::Integer)::Float64
        h = (b-a) /n
        x = a
        
        In = f(a)
        for k = 2:n
            x = x + h
            In += 2 * f(x)
        end

        return (In + f(b)) * h * 0.5
    end

    function Método_de_Romberg(f::Function, variavel_inferior::Float64, variavel_superior::Float64, order::Integer, h::Float64)::Float64
        # hs = [h / 2^i for i = 0:(order - 1)]
        # col1 = [Regra_do_Trapezio(f, variavel_inferior, variavel_superior, h) for h in hs]

        # n = length(col1)
        
        # return col1[1]

        I = zeros(order, order)

        for k = 1:order
            I[k, 1] =  trapzcomp(f, variavel_inferior, variavel_superior, order)

            for j = 1:(k - 1)
                I[k, j + 1] = (4^j * I[k, j]- I[k - 1, j]) / (4^j - 1) 
            end
        end

        return I[order, order]
    end
end