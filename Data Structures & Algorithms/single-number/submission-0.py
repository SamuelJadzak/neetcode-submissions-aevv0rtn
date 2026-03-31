class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ... existing code ...
        left = 0
        while left < len(nums):
            right = left + 1
            while right < len(nums):
                if nums[left] == nums[right]:
                    del nums[right]
                    del nums[left]
                    left -= 1  # Adjust left pointer after deletions
                    break
                right += 1
            left += 1
        return nums[0]  # The remaining number is the single one

            
            
            