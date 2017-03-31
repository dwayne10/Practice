class Solution:

    def readBinaryWatch(self, num):
        res = []
        hours = [8,4,2,1]
        mins = [32,16,8,4,2,1]
        for i in range(num + 1):
            hours_list = self.generateDigit(hours, i)
            minutes_list = self.generateDigit(mins, num - i)
            for hour in hours_list:
                if int(hour) >= 12:
                    continue
                for minute in minutes_list:
                    if int(minute) >= 60:
                        continue
                    rhs = "0" + minute if int(minute) < 10 else minute
                    res.append(hour + ":" + rhs)
        return res



    def generateDigit(self, nums, count):
        res1 = []
        self.generateDigitHelper(nums, count, 0,0, res1)
        return res1

    def generateDigitHelper(self, nums, count, pos, sum, res1):
        if count == 0:
            res1.append(str(sum))
            return

        for i in range(pos,len(nums)):
            self.generateDigitHelper(nums, count - 1, i + 1, sum + nums[i],
                                     res1)




print(Solution().readBinaryWatch(2))