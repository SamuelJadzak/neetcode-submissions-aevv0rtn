class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(left, right):
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                return helper(mid + 1, right)
            else:
                return helper(0, mid)
        return helper(0, len(nums)-1)