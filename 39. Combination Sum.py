class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(path, sum, start):
            # print(path)
            if sum == target:
                res.append(path[:])
                return
            if sum > target:
                return

            for i in range(start, len(candidates)):
                # print(path + [candidates[i]])
                if sum + candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(path, sum + candidates[i], i) # KEY LINE - NOTICE THE
                    #  CALL USING i AS THE NEXT START INDEX
                    # THIS IS BECAUSE THE SAME NUMBER CAN BE USED INFINITE
                    # TIMES
                    path.pop() # Last value added is popped
                else:
                    return

        candidates.sort()
        if candidates[0] > target:
            return []

        res = []
        start = 0
        dfs([], 0, start)
        return res

print(Solution().combinationSum([2,3,6,7], 7))


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(path, start, sum):
            if sum == target:
                if path not in res:
                    res.append(path[:])

            if sum > target:
                return

            for i in range(start, len(candidates)):
                if sum + candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(path, i + 1, sum + candidates[i])
                    path.pop()
                else:
                    return

        candidates.sort()
        res = []
        dfs([], 0, 0)
        return res

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def dfs(path, sum, start):
            if len(path) == k and sum == n:
                res.append(path[:])
                return

            for i in range(start,10):
                if sum + i <= n and len(path) + 1 <= k:
                    path.append(i)
                    dfs(path, sum + i, i + 1)
                    path.pop()
                else:
                    return
        res = []
        dfs([],0,1)
        return res


def dfs(path, sum, start):
    # print(path)
    if IsValidPath/Entry() eg: sum == target:
        res.append(path[:])
        return


    for i in range(start, len(candidates)):
        # print(path + [candidates[i]])
        if sum + candidates[i] <= target:
            path.append(candidates[i])
            dfs(path, sum + candidates[i], i)  # KEY LINE - NOTICE THE
            #  CALL USING i AS THE NEXT START INDEX
            # THIS IS BECAUSE THE SAME NUMBER CAN BE USED INFINITE
            # TIMES
            path.pop()  # Last value added is popped
        else:
            return