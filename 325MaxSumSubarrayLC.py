def maxSubArrayLen(nums, k):
    ans, acc = 0, 0               # answer and the accumulative value of nums
    mp = {0:-1}                 #key is acc value, and value is the index
    for i in range(len(nums)):
        acc += nums[i]
        if acc not in mp:
            mp[acc] = i
        if acc-k in mp:
            ans = max(ans, i-mp[acc-k])
    return ans

print(maxSubArrayLen([1,-1,5,-2,10], 2 ))