module InterpolacaoPolinomial
    function vanderMonde(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, n::Int64=length(coords_x)):: Vector{<:Real}
        return reduce(vcat, transpose.(map(x -> [x^i for i = 0:(n - 1)], coords_x))) \ coords_y
    end

    function build_polynomial_function(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, n::Int64=length(coords_x))
        return build_polynomial_function!(vanderMonde(coords_x, coords_y, n))
    end

    function build_polynomial_function!(coefs::Vector{<:Real})
        return x::Real -> sum([valor * x^index for (_, (index, valor)) in enumerate(zip(collect(0:(length(coefs) - 1)), coefs))])
    end
end