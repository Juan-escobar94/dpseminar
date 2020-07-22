INF = 1 << 32

#p = [30, 35, 15, 5, 10, 20, 25]
p = [4, 5, 2, 3, 5]


def matrix_chain_order(p):

    n = len(p)
    m = [[INF] * (n-1) for x in range(n-1)]  # store optimal costs value
    # store k value to reconstruct solution
    s = [[0] * (n-1) for x in range(n-1)]
    for i in range(0, n-1):
        m[i][i] = 0
    for l in range(2, n):
        for i in range(0, n-l):
            j = i + l - 1
            # 5m[i][j] = INF
            for k in range(i, j):
                t1 = m[i][k]
                t2 = m[k+1][j]
                prod = p[i]*p[k+1]*p[j+1]
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if (q < m[i][j]):
                    m[i][j] = q
                    s[i][j] = k
    return (m, s)


(sol, rec) = matrix_chain_order(p)


def printOptimal(s, i, j):
    if i == j:
        print("A_" + str(i+1), end='')
    else:
        print("(", end='')
        printOptimal(s, i, s[i][j])
        printOptimal(s, s[i][j]+1, j)
        print(")", end='')


printOptimal(rec, 0, 3)
print("\n")
