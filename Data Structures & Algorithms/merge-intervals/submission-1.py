class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l, r = 0, 1
        intervals.sort(key= lambda interval: interval[0])
        while r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][0] = min(intervals[l][0], intervals[r][0])
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                del intervals[r]
            else:
                l=l+1
                r=r+1
        return intervals