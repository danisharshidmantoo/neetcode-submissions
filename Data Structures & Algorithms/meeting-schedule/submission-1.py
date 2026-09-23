"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        if len(intervals) == 0:
            return True
        critical = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < critical:
                return False
           
            critical = interval.end
        return True