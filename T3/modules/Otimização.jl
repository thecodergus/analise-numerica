module Otimização
    function regra_do_trapezio(f::Function, a::Float64, b::Float64; n::Int64 = 256, h::Float64 = abs(b - a) / n)::Float64
        return (f(a) + 2 * (sum(map(x -> f(a + x * h), collect(1:(n - 1))))) + f(b)) * (h / 2)
    end

    function melhor_função(f::Function, funcs::Vector{Function}, a::Float64, b::Float64; 
                            n::Int64 = 256, 
                            k::Int64 = length(funcs), 
                            A::Matrix{Float64} = zeros(k, k), 
                            B::Vector{Float64} = zeros(k))::Vector{Float64}

            for i = 1:(k -1)
                for j = 1:(k - 1)
                    if j >= i
                    A[i, j] = regra_do_trapezio(x -> funcs[i](x) * funcs[j](x), a, b; n = n)
                    else
                        A[i, j] = A[j, i]
                    end
                end
                B[i] = regra_do_trapezio(x -> f(x) * funcs[i](x), a, b; n = n)
            end
        
        return A \ B
    end

end