class Solution:

    def generateDigit(self, vals, count):
        numbers = []
        self.generateDigitDFS(vals, count, 0, 0, numbers)
        return numbers

    def generateDigitDFS(self, vals, count, position, total, numbers):
        if count == 0:
            numbers.append(total)
            return

        for i in range(position, len(vals)):
            self.generateDigitDFS(vals, count - 1, i + 1,
                                  total + vals[i], numbers)

    def readBinaryWatch(self, num):
        res = []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]

        for i in range(num + 1):
            valid_hours = self.generateDigit(hours, i)
            valid_minutes = self.generateDigit(minutes, num - i)

            # print(valid_hours)
            for h in valid_hours:
                if h >= 12:
                    continue
                    for m in valid_minutes:
                        if m >= 60:
                            continue
                        if m > 10:
                            rhs = str(m)
                        else:
                            rhs = '0' + str(m)

                        res.append(str(h) + ":" + rhs)

        # print(res)
        return res
print(Solution().readBinaryWatch(3))
