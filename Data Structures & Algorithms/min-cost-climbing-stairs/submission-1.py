class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res = 0
        def helper(step):
            if step > len(cost)-1:
                return 0
            return min(cost[step] + helper(step+1), cost[step] + helper(step+2))
        return min (helper(0), helper(1))
        