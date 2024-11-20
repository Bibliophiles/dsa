def flippingMatrix(matrix):
    n = len(matrix) // 2
    return sum(
        max(matrix[i][j], matrix[~i][j], matrix[i][~j], matrix[~i][~j])
        for i in range(n) for j in range(n)
    )
