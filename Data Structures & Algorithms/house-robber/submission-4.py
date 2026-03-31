# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         from functools import lru_cache

#         @lru_cache(None)
#         def helper(start_ind):
#             if start_ind >= len(nums):
#                 return 0
#             return max(helper(start_ind + 1), nums[start_ind] + helper(start_ind + 2))


class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(start_ind):
            if start_ind >= len(nums):
                return 0
            if start_ind in memo:
                return memo[start_ind]
            
            result = max(helper(start_ind + 1), nums[start_ind] + helper(start_ind + 2))
            memo[start_ind] = result
            return result

        return helper(0)