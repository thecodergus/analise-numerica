module Derivada
    function calc_coefs(x0::Float64, coords_x::Vector{<:Float64}; ordem::Integer = 1)::Vector{Float64}
        n::Integer = length(coords_x)
        A::Matrix{Float64}, B::Vector{Float64} = ones(1, n), zeros(1)

        for i = 1:(n - 1)
            A = vcat(A, (coords_x .^ i)')

            if i < ordem
                push!(B, 0)
            elseif i == ordem
                push!(B, factorial(ordem))
            else
                push!(B, (factorial(i) / factorial(i - ordem)) * x0^(i - ordem))
            end
        end

        return A \ B
    end

    function derivada_finita(f::Function, x0::Float64, coords_x::Vector{<:Float64}; ordem::Integer = 1, coords_y::Vector{<:Float64} = f.(coords_x))::Float64
        return sum(calc_coefs(x0, coords_x; ordem=ordem) .* coords_y)
    end

    function taylor_series(f::Function, x0::Float64, xp::Float64, coords_x::Vector{<:Float64}; ordem::Integer = 1, coords_y::Vector{<:Float64} = f.(coords_x))::Float64
        return f(x0) + sum([(derivada_finita(f, x0, coords_x; ordem = i, coords_y = coords_y) / factorial(i)) * (xp - x0)^i for i = 1:ordem])
    end

    function extrapolação_Richardson!(coluna::Vector{Float64})::Float64
        n = length(coluna)

        for i = 1:n, j = 1:((n - 1) - (i - 1))
            coluna[j] = (2^i * coluna[j + 1] - coluna[j]) / (2^i - 1)
        end

        return coluna |> first
    end

    function extrapolação_Richardson(f::Function, x0::Float64; ordem::Integer = 1, h::Float64 = 0.0001)::Float64
        df(h2) = (f(x0 + h2) - f(x0)) / h2

        coluna = df.(fill(h, ordem) ./ (fill(2, ordem) .^ collect(0:(ordem-1))))

        return extrapolação_Richardson!(coluna)
    end

    function extrapolação_Richardson(aproximações::Vector{Float64})::Float64
        return extrapolação_Richardson!([aproximações;extrapolação_Richardson!(copy(aproximações))])
    end

    
end
