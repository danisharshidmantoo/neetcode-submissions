"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n== 0:
            return 0
        intervals.sort(key = lambda x: x.end)
        heap = []
        heapq.heappush(heap,intervals[0].end)
        for interval in intervals:
            minend = heapq.heappop(heap)
            if interval.start>= minend:
                heapq.heappush(heap,interval.end)
            else:
                heapq.heappush(heap,interval.end)
                heapq.heappush(heap,minend)
        return len(heap)-1
            
