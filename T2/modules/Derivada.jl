module Derivada
    function derivada_finita(f::Function, x0, coords_x; ordem::Integer = 1)
        n::Integer, coords_y = length(coords_x), f.(coords_x)
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

        return sum(coeffs .* coords_y)
    end
end
