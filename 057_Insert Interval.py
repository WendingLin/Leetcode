#57.Insert Interval
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
    #My Solution(Not solved for border situation)
        """
        if newInterval==None:
            return intervals
        length=len(intervals)
        if length==0 or newInterval.start>intervals[length-1].end:
            intervals.append(Interval(newInterval.start,newInterval.end))
            return intervals
        loca=0
        #Find the location of start point
        while loca<length:
            if newInterval.start>intervals[loca].start:
                loca+=1
            else:
                break

        #Find the location of end point
        if loca==0 or newInterval.start>intervals[loca-1].end:
            if newInterval.end<intervals[loca].start:
                intervals.insert(loca, newInterval)
                return intervals
            while loca+1<length:
                if intervals[loca].start<newInterval.end<intervals[loca].end:
                    intervals[loca].start=newInterval.start
                    break
                elif intervals[loca].end<newInterval.end<intervals[loca+1].start:
                    intervals[loca].start=newInterval.start
                    intervals[loca].end=newInterval.end
                    break
                else:
                    del intervals[loca]
                    length-=1
            if loca+1==length:
                #Exclude the situation of the last element
                if newInterval.end<intervals[loca].end:
                    intervals[loca].start=newInterval.start
                else:
                    intervals[loca].start = newInterval.start
                    intervals[loca].end = newInterval.end
        else:
            if newInterval.end<intervals[loca-1].end:
                return intervals
            while loca<length:
                if intervals[loca-1].end<newInterval.end<intervals[loca].start:
                    intervals[loca-1].end=newInterval.end
                    break
                elif intervals[loca].start<newInterval.end<intervals[loca].end:
                    intervals[loca-1].end=intervals[loca].end
                    del intervals[loca]
                    break
                else:
                    del intervals[loca]
                    length-=1
            if loca==length:
                #Exclude the situation of the last element
                intervals[loca - 1].end = newInterval.end
        return intervals
        """
        #My Modified Solution
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)
        res=[]
        for i in range(len(intervals)):
            if res==[]:
                res.append(intervals[i])
            else:
                length=len(res)
                if res[length-1].start<=intervals[i].start<=res[length-1].end:
                    res[length-1].end=max(res[length-1].end, intervals[i].end)
                else:
                    res.append(intervals[i])
        return res
        """
        #Improved Solution
        res=[]
        insert_pos=0
        for interval in intervals:
            if interval.end<newInterval.start:
                res.append(interval)
                insert_pos+=1
            elif interval.start>newInterval.end:
                res.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        res.insert(insert_pos, newInterval)
        return res