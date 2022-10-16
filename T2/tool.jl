using Printf

function printItem(item::Number)
    @printf "%.7f,\n" item
end

function printMatrix(matrix::AbstractMatrix)
    tam = size(matrix)

    for i = 1:tam[1]
        for j = 1:tam[2]
            printItem(matrix[i, j])
        end
    end
end

function printVector(v::AbstractVector)
    for i = v
        printItem(i)
    end
end