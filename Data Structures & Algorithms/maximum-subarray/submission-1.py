class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = -1001
        while r < len(nums):
            cur_sum = sum(nums[l:r+1])
            res = max(res, cur_sum)
            if cur_sum < 0:
                l = r + 1
            r += 1
        return res