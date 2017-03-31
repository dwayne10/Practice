# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals

        # critical step - sort by start time
        intervals.sort(key=lambda x: x.start)
        res = []

        res.append(intervals[0])
        # print(res[0])
        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            prev_s, prev_e = res[len(res) - 1].start, res[len(res) - 1].end
            if start > prev_e:
                res.append(Interval(start, end))
            else:
                res[len(res) - 1] = Interval(prev_s, max(prev_e, end))
        return res



