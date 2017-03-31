def longestIncreasingSubsequence(arr):
    if not arr:
        return 0

    res = [1] * len(arr) # minumum increasing length is 1 not zero !
    for i in range(1, len(arr)):
        for j in range(0,i):
            if arr[j] <= arr[i]:
                res[i] = max(res[j] + 1, res[i])

    print(res)
    return max(res)


print(longestIncreasingSubsequence([3,4,-1,0,6,2,3]))

