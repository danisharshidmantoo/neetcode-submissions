"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        l = r = 0
        maxcount = 0
        count = 0
        while l<len(start):
            #process the end point
            if start[l]>=end[r]:
                count -= 1
                r += 1
            else:
                l += 1
                count += 1
                maxcount = max(maxcount,count)
        return maxcount