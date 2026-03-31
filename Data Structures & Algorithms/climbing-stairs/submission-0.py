class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(i, memo):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            memo[i] = solve(i + 1, memo) + solve(i + 2, memo)
            return memo[i]
        return solve(0, {})