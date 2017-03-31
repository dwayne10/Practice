'''

Assume you have an array of length n initialized with all 0's and are given k update operations.+

Each operation is represented as a triplet: [startIndex, endIndex, inc]
which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.
Example:
Given:
    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]
Output:
    [-2, 0, 3, 5, 3]
Explanation:
Initial state: [ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]: [ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]: [ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]: [-2, 0, 3, 5, 3 ]



'''
class Solution(object):
    # def getModifiedArray(self, length, updates):
    #     arr = [0]*length
    #     for row in updates:
    #         inc = row[2]
    #         start, end = row[0] , row[1]
    #         for x in range(start,end+1):
    #             arr[x] += inc
    #     # print(arr)
    #     return arr
    def getModifiedArray(self, length, updates):

        # Collect the events, i.e., what changes happen and when they happen
        increaseAt = [0] * length
        decreaseAfter = [0] * length
        for start, end, inc in updates:
            increaseAt[start] += inc
            decreaseAfter[end] += inc

        # Sweep, i.e., walk the range, updating the current value and storing it in the output array
        outputArray = [None] * length
        currentValue = 0
        for index in range(0, length):
            currentValue += increaseAt[index]
            outputArray[index] = currentValue
            currentValue -= decreaseAfter[index]

        # Ship it
        return outputArray


updates = [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
]
print(Solution().getModifiedArray(5, updates))








