# class Solution:
#     # @param A : list of integers
#     # @return a list of list of integers
#     def subsets(self, A):
#         def permute(A, path, start, end):
#             res.append(path[:])
#             print(res)
#
#             for i in range(start, len(A)):
#                 path.append(A[i])
#                 permute(A, path, i + 1, len(A))
#                 path.pop()
#
#         res = []
#         path = []
#         A.sort()
#         permute(A, path, 0, len(A))
#
#         return res
#
#
# print(Solution().subsets([1,2,3]))


# class Solution:
#     # @param n : integer
#     # @param k : integer
#     # @return a list of list of integers
#     def combine(self, n, k):
#
#         def backtrack(path, start, end, k):
#             if len(path) == k:
#                 res.append(path[:])
#
#             for i in range(start, end):
#                 backtrack(path + [i], i + 1, end, k)
#
#         res = []
#         path = []
#         backtrack([], 1, n + 1, k)
#         return res
#
# print(Solution().combine(4,2))


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):

        def permuteHelper(A, start, end):
            if start == len(A):
                res.append(A[:])

            for i in range(start, end):
                A[i], A[start] = A[start], A[i]
                permuteHelper(A, start + 1, end)
                A[i], A[start] = A[start], A[i]

        res = []

        permuteHelper(A, 0, len(A))
        return res

print(Solution().permute([1,2,3, 4]))