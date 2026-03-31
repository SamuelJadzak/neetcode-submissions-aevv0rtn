class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def helper(intervals):
            l, r = 0, 1
            while r < len(intervals):
                print(intervals[l])
                print(intervals[r])
                if intervals[l][1] >= intervals[r][0]:
                    intervals[l][0] = min(intervals[l][0], intervals[r][0])
                    intervals[l][1] = max(intervals[l][1], intervals[r][1])
                    del intervals[r]
                else:
                    l=l+1
                    r=r+1
            return intervals

        if not intervals:
            intervals.insert(0, newInterval)
            return intervals


        for i, interval in enumerate(intervals):
            if newInterval[0] < interval[0]:
                intervals.insert(i, newInterval)
                break
            elif i == len(intervals)-1:
                intervals.append(newInterval)
                break
        print(intervals)


        return helper(intervals)


