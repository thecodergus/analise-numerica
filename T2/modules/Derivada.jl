module Derivada
    function derivada_finita(f::Function, x0::Real, coords_x::Vector{<:Real}; ordem::Integer = 1)::Real
        n::Integer = length(coords_x)
        A::Matrix{Real}, B::Vector{Real} = ones(1, n), zeros(1)

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

        coeffs = A \ B

        println(f.(coords_x))
        return sum(coeffs .* f.(coords_x))
    end
end
