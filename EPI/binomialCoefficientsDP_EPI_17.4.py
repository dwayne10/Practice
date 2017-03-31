def nChoosek(n,k):
    def nChoosekHelper(n,k,coefficients):

        # base case
        if n == k or k == 0:
            return 1

        if coefficients[n][k] == 0:
            with_item = nChoosekHelper(n-1, k-1, coefficients)
            without_item = nChoosekHelper(n-1, k, coefficients)
            coefficients[n][k] = with_item + without_item
        return coefficients[n][k]

    coefficients = [[0]*(k+1) for _ in range(n+1)]
    print(nChoosekHelper(n,k,coefficients))

nChoosek(10,2)