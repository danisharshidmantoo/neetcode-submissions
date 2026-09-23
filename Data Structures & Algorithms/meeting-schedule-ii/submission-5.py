"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = [interval.start for interval in intervals]
        endTime = [interval.end for interval in intervals]
        startTime.sort()
        endTime.sort()
        s,e = 0,0
        count = 0
        result = 0
        while s<len(startTime):
            if startTime[s]<endTime[e]:
                s += 1
                count += 1
                result = max(result,count)
            elif endTime[e]<=startTime[s]:
                e += 1
                count -= 1
        return result