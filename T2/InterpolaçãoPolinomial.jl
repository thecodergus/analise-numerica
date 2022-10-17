
module InterpolaçãoPolinomial
    include("tool.jl")
    vector_of_vectors_to_matrix(a) = reduce(vcat,transpose.(a))

    function vanderMonde(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64):: Vector{<:Real}
        return vector_of_vectors_to_matrix(map(x -> [x^i for i = 0:grau], coords_x)) \ coords_y
    end

    # Ajusto de curva comum - Regressão Linear
    function AjusteDeCurva(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64)
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y

        return (X, coefs, Y)
    end

    # Ajuste a uma curva exponencial - Regressão Linear
    # y = a*(e^b*x) <=> ln y = ln a + b*x 
    # adaptação: y = a*(t^b*x) onde t e seu log log correspondete variam
    # Questão chata pra caralho, questão: Q12 de Ajuste de Curvas
    function AjusteDeCurvaExponencial(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64 = 1; t = ℯ, ant_t = log)
        # pq Y = ln y
        map!(ant_t, coords_y, coords_y)
        
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y

        coefs_cp = copy(coefs)
        coefs[1] = t^coefs[1]
        
        # Retornar os coeficientes, e a função adaptada para a situação
        return (coefs, x::Real -> t^(sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs_cp)])))
    end

    # Ajuste a uma curva geométrica - Regressão Linear
    # Para funções do tipo y = a*x^b <=> ln y = ln a + x*ln b = a + b*x
    function AjusteDeCurvaGeométrica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64 = 1; t = ℯ, ant_t = log)
        map!(ant_t, coords_y, coords_y)
        map!(ant_t, coords_x, coords_x)

        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y


        coefs_cp = copy(coefs)
        coefs[1] = t^coefs[1]

        # Coeficientes e a função adaptada
        return (coefs, x::Real -> t^(sum([valor * ant_t(x)^index for (index, valor) in zip(Iterators.countfrom(0), coefs_cp)])))
    end

    # Ajusto de curva hiperbolica - Regressão Linear
    # z = 1/y = a + b*x
    function AjusteDeCurvaHiperbolica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64)
        map!(y -> 1 / y, coords_y, coords_y)
        
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y

        return coefs
    end

    function build_polynomial_function(coefs::Vector{<:Real})::Function
        return x::Real -> sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs)])
    end
end