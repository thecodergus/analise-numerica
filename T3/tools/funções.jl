
module funções
    using PythonCall
    math = pyimport("math")

    macro expr2fn(fname, expr, args...)
        fn = quote
            function $(esc(fname))()
                $(esc(expr.args[1]))
            end
        end
        for arg in args
            push!(fn.args[2].args[1].args, esc(arg))
        end
        return fn
    end

    function criar_função(f::String)::Function
        return @eval x -> $(f |> Meta.parse)
    end

    function map_function(arr::Vector{String})::Vector{Function}
        return criar_função.(arr)    
    end

    export criar_função
end