"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: interval.start)
        res = 0
        while intervals:
            window = Interval(-1, 0)
            removetimes = []
            for i, time in enumerate(intervals):
                if time.start >= window.end:
                    window.end = time.end
                    removetimes.append(i)
            for time in sorted(removetimes, reverse=True):
                intervals.pop(time)
            res+=1 
        return res
                

        
        