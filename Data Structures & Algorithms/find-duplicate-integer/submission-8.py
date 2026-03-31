class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect the cycle
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]  # Move slow pointer by 1 step
            fast = nums[nums[fast]]  # Move fast pointer by 2 steps
            if slow == fast:  # Cycle detected
                break

        # Step 2: Find the entry point of the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]  # Move both pointers by 1 step
            fast = nums[fast]
        
        return slow

