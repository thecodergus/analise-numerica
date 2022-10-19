
module InterpolaçãoPolinomial
    vector_of_vectors_to_matrix(a) = reduce(vcat,transpose.(a))

    function vanderMonde(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64):: Vector{<:Real}
        return vector_of_vectors_to_matrix(map(x -> [x^i for i = 0:grau], coords_x)) \ coords_y
    end

    # Ajusto de curva comum - Regressão Linear
    function AjusteDeCurva(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1)
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y

        return (coefs, build_polynomial_function(coefs))
    end

    # Ajuste a uma curva exponencial - Regressão Linear
    # y = a*(e^b*x) <=> ln y = ln a + b*x 
    # adaptação: y = a*(t^b*x) onde t e seu log log correspondete variam
    # Questão chata pra caralho, questão: Q12 de Ajuste de Curvas
    function AjusteDeCurvaExponencial(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        # pq Y = ln y
        coords_y = ant_t.(coords_y)
        
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y
 
        # coefs_cp = copy(coefs)
        # coefs[1] = t^coefs[1]
        
        # Retornar os coeficientes, e a função adaptada para a situação
        return (coefs, x::Real -> t^(sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs)])))
    end

    # Ajuste a uma curva exponencial 2 - Regressão Linear
    # y = a*x*(e^b*x) <=> ln y = ln a + ln x + b*x 
    function AjusteDeCurvaExponencial2(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        # pq Y = ln y
        coords_y = ant_t.(coords_y)
        coords_x = ant_t.(coords_x)
        
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
    function AjusteDeCurvaGeométrica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        coords_y = ant_t.(coords_y)
        coords_x = ant_t.(coords_x)

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
    # y = a*(x / (x + b)) => 1/y = 1/a + b/(a * x) <=> 1/y = a + b*x
    # z = 1/y = a + b*x
    function AjusteDeCurvaHiperbolica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1)
        coords_x = inv.(coords_x) 
        coords_y = inv.(coords_y) 
        # esquerdo da equação
        X = vector_of_vectors_to_matrix([[sum(map(x -> x^(i + j), coords_x)) for j in 0:grau] for i in 0:grau])
        # direito da equação
        Y = vector_of_vectors_to_matrix([sum([yi * xi^i for (xi, yi) = zip(coords_x, coords_y)]) for i = 0:grau]) 
        # coeficiente gerados
        coefs = X \ Y

        coefs_cp = copy(coefs)
        coefs[1] = inv(coefs[1])
        coefs[2] *= coefs[1]

        return (coefs, x::Real -> inv(sum([valor * inv(x)^index for (index, valor) in zip(Iterators.countfrom(0), coefs_cp)])))
    end

    # Codigo que o Luas fez, entendo nada sobre o que ta rolando aqui dentro
    function lucas(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64)
        p = [(a, b) for (a, b) in zip(coords_x, coords_y)]

        X(p) = vcat([[1 i[1]] for i in p])
        Y(p) = [log(i[2]) for i in p]

        β = inv(X(p)' * X(p)) * X(p)' * Y(p)

        β_final = [exp(β[1]), β[2]]

        return β_final
    end

    function build_polynomial_function(coefs::Vector{<:Real})::Function
        return x::Real -> sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs)])
    end
end