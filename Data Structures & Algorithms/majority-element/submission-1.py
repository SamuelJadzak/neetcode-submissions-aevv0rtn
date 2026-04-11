class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Input: nums = [5,1,1]
        d = {}
        majority_elem = nums[0]
        for elem in nums:
            # ocurrences = d.get(elem, 0)
            if d.get(majority_elem, 0) < d.get(elem, 0):
                majority_elem = elem
            d[elem] = d.get(elem, 0) + 1

        return majority_elem



        