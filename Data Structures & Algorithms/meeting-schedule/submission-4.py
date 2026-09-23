"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        e = -1
        conflicts = 0
        for interval in intervals:
            start,end = interval.start,interval.end
            if start<e:
                return False
            e = end
        return True