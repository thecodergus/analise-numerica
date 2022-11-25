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

function criar_funçã(f::String; parametros = [])::Function
    return @eval $(build_function(expand_derivatives(Differential(x)(f)), x))    
end
