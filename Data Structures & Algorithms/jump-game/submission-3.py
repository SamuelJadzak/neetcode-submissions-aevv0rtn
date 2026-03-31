class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        def helper(i):
            nonlocal res
            if i >= len(nums)-1:
                res = True
                return
            if i < len(nums)-1 and nums[i] == 0:
                return
            for j in range(1, nums[i]+1):
                helper(i+j)
        helper(0)
        return res

        