"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
      start = sorted(interval.start for interval in intervals)
      end = sorted(interval.end for interval in intervals)  

      maxrooms = 0
      l = 0
      r = 0
      count = 0
      while l<len(start):
        if start[l] >= end[r]:
            r += 1
            count -= 1
        else:
            l += 1
            count += 1
            maxrooms = max(maxrooms,count)
      return maxrooms