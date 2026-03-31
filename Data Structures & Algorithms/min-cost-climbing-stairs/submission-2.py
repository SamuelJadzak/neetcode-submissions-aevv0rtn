class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        def helper(step, cache):
            if step > len(cost)-1:
                return 0
            if step in cache:
                return cache[step]
            cache[step] = min(cost[step] + helper(step+1, cache), cost[step] + helper(step+2, cache))
            return cache[step]
        return min (helper(0, {}), helper(1, {}))
        