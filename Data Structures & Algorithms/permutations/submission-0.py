class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = self.helper(nums, [])
        return self.res

    def helper(self, nums, perm):
        if not nums:
            self.res.append(perm.copy())
            return
        for i, num in enumerate(nums):
            perm.append(num)
            self.helper(nums[:i] + nums[i+1:], perm)
            perm.pop()
            

