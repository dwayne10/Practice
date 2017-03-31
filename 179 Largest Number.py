class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):

        out = [str(n) for n in nums]
        # out.sort(key=lambda x: x)
        print(out)

        buckets = [[]] * 10  # 0-9 digits

        for n in out:
            msb = int(n[0])
            if buckets[msb] == []:
                buckets[msb] = [n]
            else:
                buckets[msb].append(n)

        print(buckets)

        res = ""
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != []:
                if len(buckets[i]) == 1:
                    res += buckets[i][0]
                else:
                    vals = buckets[i]
                    vals.sort(cmp=lambda x, y: cmp(y + x, x + y)) # Most important step the compare function
                    for v in vals:
                        res += v
        if res[0] == '0' and len(res) != 1:
            return "0"
        return res