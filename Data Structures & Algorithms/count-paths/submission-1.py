class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j, cache):
            if (i,j) in cache:
                return cache[(i,j)]
            if i > m-1 or j > n-1:
                return 0
            if i == m-1 and j == n-1:
                return 1

            cache[(i,j)] = helper(i, j+1, cache) + helper(i+1, j, cache)
            return cache[(i,j)]

        return helper(0,0, {})