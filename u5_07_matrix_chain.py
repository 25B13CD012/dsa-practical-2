def matrix_chain(dims):
    n = len(dims) - 1

    cost = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float("inf")

            for k in range(i, j):
                c = (
                    cost[i][k]
                    + cost[k + 1][j]
                    + dims[i] * dims[k + 1] * dims[j + 1]
                )

                if c < cost[i][j]:
                    cost[i][j] = c
                    split[i][j] = k

    return cost, split


def parens(split, i, j):
    if i == j:
        return "A" + str(i + 1)

    k = split[i][j]

    return (
        "("
        + parens(split, i, k)
        + " x "
        + parens(split, k + 1, j)
        + ")"
    )


dims = [10, 30, 5, 60]

cost, split = matrix_chain(dims)

print("Minimum multiplications:", cost[0][-1])
print("Best order:", parens(split, 0, len(dims) - 2))
