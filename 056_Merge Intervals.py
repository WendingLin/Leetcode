#56.Merge Intervals
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
        #My Solution
        intervals.sort(key=lambda x:x.start)
        res=[]
        for interval in intervals:
            if res==[]:
                res.append(interval)
            else:
                length=len(res)
                if res[length-1].start<=interval.start<=res[length-1].end:
                    res[length-1].end=max(res[length-1].end,interval.end)
                else:
                    res.append(interval)
        return res