
module InterpolaçãoPolinomial
    vector_of_vectors_to_matrix(a) = reduce(vcat,transpose.(a))
    
    function vanderMonde(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64):: Vector{<:Real}
        return vector_of_vectors_to_matrix(map(x -> [x^i for i = 0:grau], coords_x)) \ coords_y
    end

    function regressão_linear(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64)
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        return (X, X \ Y, Y)
    end

    function build_polynomial_function(coefs::Vector{<:Real})::Function
        return x::Real -> sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs)])
    end
end