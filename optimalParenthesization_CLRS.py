def optimalParenthesMxMult(p):
    '''
            p is a list of matrix dimensions
    '''

    n = len(p) - 1  # number of matrices

    # create a n * n  matrix m for storing the costs

    maxi = float('inf')
    m = [[maxi] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        m[i][i] = 0  # set diagonal to zeroes - these are subsets of length 1

    for i in range(n + 1):
        m[0][i] = 0

    for i in range(n + 1):
        m[i][0] = 0

    for length in range(2, n + 1):   # length is the subseq length
        for i in range(1, n - length + 2):  # max value of i can be n - length + 1
            j = i + length - 1

            for k in range(i, j):
                res = m[i][k] + m[k + 1][j] + (p[i - 1] * p[k] * p[j])
                if res < m[i][j]:
                    m[i][j] = res
    return m

print(optimalParenthesMxMult([30, 35, 15, 5, 10, 20, 25]))
