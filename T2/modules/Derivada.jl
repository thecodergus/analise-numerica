module Derivada
    function derivada_finita(f::Function, x0, coords_x; ordem::Integer = 1)
        n::Integer = length(coords_x)
        coords_y = f.(coords_x)

        A::Matrix{Real}, B::Vector{Real} = ones(1, n), [0.0]

        for i = 1:(n - 1)
            row_i = coords_x .^ i
            A = vcat(A, row_i')

            if i < ordem
                push!(B, 0)
            elseif i == ordem
                push!(B, factorial(ordem))
            else
                numer, denom = factorial(i), factorial(i - ordem)

                el = (numer / denom) * x0^(i - ordem)

                push!(B, el)
            end
        end

        coeffs = A \ B

        return sum(coeffs .* coords_y)
    end
end
