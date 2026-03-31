"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i, time1 in enumerate(intervals):
            for time2 in intervals[:i]+intervals[i+1:]:
                if time2.start <= time1.start < time2.end:
                    return False
                if time2.start < time1.end < time2.end:
                    return False
        return True

