
# Resumo gera: y = a + b*x

module AjusteDeCurvas
    using Polynomials
    vector_of_vectors_to_matrix(a) = reduce(vcat,transpose.(a))

    function vanderMonde(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64):: Vector{<:Real}
        return vector_of_vectors_to_matrix(map(x -> [x^i for i = 0:grau], coords_x)) \ coords_y
    end

    function gerarCoefs(x::Vector{<:Real}, y::Vector{<:Real}, grau::Int64)
        # Ta na mão de Deus
        return fit(x, y, grau) |> coeffs
    end

    function gerarCoefs!(x::Vector{<:Real}, y::Vector{<:Real}, g::Int64)
        # Gerar de forma Chata
        # lado esquerdo da equação
        X = [sum(x .^ (i + j)) for i = 0:g, j = 0:g]
        # lado direito da equação
        Y = [sum(y .* (x .^ i)) for i = 0:g]

        return X \ Y

    end 

    # Ajusto de curva comum - Regressão Linear
    function AjusteDeCurva(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1)
        coefs = gerarCoefs(coords_x, coords_y, grau)

        # return (coefs, build_polynomial_function(coefs, grau))
        return (coefs, x::Real -> sum(coefs .* (x .^ collect(0:grau))))
    end

     #=
        Ajusto de curva comum 2 - Regressão Linear
        x = ℯ^((y - b)/a) <=> y = b + a * ln x
    =#
    function AjusteDeCurva2(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1)
        coords_x = log.(coords_x)

        coefs = gerarCoefs(coords_x, coords_y, grau)

        coefs_cp = copy(coefs)
        coefs[1], coefs[2] = coefs[2], coefs[1]

        return (coefs, x::Real -> sum(coefs_cp .* (log(x) .^ collect(0:grau))))
    end

     #=
        Ajusto de curva comum 3 - Regressão Linear
        y = ((a + √x)/(b*√x))^2 <=> y⁻¹ = b⁻¹ + a * b⁻¹ * (√x)⁻¹
    =#
    function AjusteDeCurva3(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1)
        x = coords_x
        Y = sqrt.(coords_y)

        # coefs = gerarCoefs(coords_x, coords_y, grau)

        # Do lucas
        A = reduce(vcat, [[i^(-1/2) 1] for i in x])
        A, B = (A' * A) \ (A' * Y)

        b = inv(B)
        a = A*b
        coefs = [a, b]
        coefs_cp = copy(coefs)

        # return (coefs, x::Real -> sum(coefs_cp .* ((x^(-1/2)) .^ collect(0:grau))))
        return (
            coefs,
            x -> b + a*x^(-1/2)
        )
    end

    #=
    Ajuste a uma curva exponencial - Regressão Linear
    y = a*(e^b*x) <=> ln y = ln a + b*x 
    adaptação: y = a*(t^b*x) onde t e seu log log correspondete variam
    Questão chata pra caralho, questão: Q12 de Ajuste de Curvas
    =#
    function AjusteDeCurvaExponencial(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        # pq Y = ln y
        coords_y = ant_t.(coords_y)
        
        coefs = gerarCoefs(coords_x, coords_y, grau)
 
        # coefs_cp = copy(coefs)
        # coefs[1] = t^coefs[1]
        
        # Retornar os coeficientes, e a função adaptada para a situação
        return (coefs, x::Real -> t^(sum(coefs .* (x .^ collect(0:grau)))))
        # return (coefs, x::Real -> t^(sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs)])))
    end

    #=
    Ajuste a uma curva exponencial 2 - Regressão Linear
    y = a*x*(e^b*x) <=> ln y = ln a + ln x + b*x  => ln y - ln x = ln a + b*x <=> ln (y/x) = ln a + b*x
    Fonte: https://math.stackexchange.com/questions/2005899/is-it-possible-to-linearize-y-axebx-in-a-linear-regression
    https://www.mathworks.com/matlabcentral/answers/540219-i-am-having-trouble-finding-the-curve-fit-of-an-equation-in-matlab
    =#
    function AjusteDeCurvaExponencial2(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        # pq Y = ln y
        y2 = ant_t.(coords_y) - ant_t.(coords_x)

        coefs = gerarCoefs(coords_x, y2, grau)

        coefs_cp = copy(coefs)
        coefs[1] = t^coefs[1]
        
        # Retornar os coeficientes, e a função adaptada para a situação
        return (coefs, x::Real -> t^(sum(coefs_cp .* (x .^ collect(0:grau)))) * x)
        # return (coefs, x::Real -> t^(sum([valor * x^index for (index, valor) in zip(Iterators.countfrom(0), coefs_cp)]))*x)
    end

    #=
    Ajuste a uma curva geométrica - Regressão Linear
    Para funções do tipo y = a*x^b <=> ln y = ln a + x*ln b = a + b*x
    =#
    function AjusteDeCurvaGeométrica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, t = ℯ, ant_t = log)
        coords_y = ant_t.(coords_y)
        coords_x = ant_t.(coords_x)

        coefs = gerarCoefs(coords_x, coords_y, grau)

        coefs_cp = copy(coefs)
        coefs[1] = t^coefs[1]

        # Coeficientes e a função adaptada
        # return (coefs, x::Real -> t^(sum([valor * ant_t(x)^index for (index, valor) in zip(Iterators.countfrom(0), coefs_cp)])))
        return (coefs, x::Real -> t^(sum(coefs_cp .* (ant_t(x) .^ collect(0:grau)))))
    end

    #=
    Ajusto de curva hiperbolica - Regressão Linear
    y = a*(x / (x + b)) => 1/y = 1/a + b/(a * x) <=> 1/y = a + b*x
    z = 1/y = a + b*x
    =#
    function AjusteDeCurvaHiperbolica(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}; grau::Int64 = 1, expoente_x = 1)
        coords_x = inv.(coords_x .^ expoente_x)
        coords_y = inv.(coords_y) 

        coefs = gerarCoefs(coords_x, coords_y, grau)

        coefs_cp = copy(coefs)
        coefs[1] = inv(coefs[1])
        coefs[2] *= coefs[1]

        return (coefs, x::Real -> inv(sum(coefs_cp .* (inv(x^expoente_x) .^ collect(0:grau)))))
    end

    #=
    Codigo que o Luas fez, entendo nada sobre o que ta rolando aqui dentro
    =#
    function lucas(coords_x::Vector{<:Real}, coords_y::Vector{<:Real}, grau::Int64)
        p = [(a, b) for (a, b) in zip(coords_x, coords_y)]

        X(p) = vcat([[1 i[1]] for i in p])
        Y(p) = [log(i[2]) for i in p]

        β = inv(X(p)' * X(p)) * X(p)' * Y(p)

        β_final = [exp(β[1]), β[2]]

        return β_final
    end

    function build_polynomial_function(coefs::Vector{<:Real}, grau::Int64)::Function
        return x::Real -> sum(coefs .* (x .^ collect(0:grau)))
    end
end