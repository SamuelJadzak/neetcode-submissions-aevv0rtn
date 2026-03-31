class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def helper(index, combination, combsum):
            if combsum == target:
                res.append(combination.copy())
                return
            if combsum > target or index >= len(candidates):
                return
            combination.append(candidates[index])
            helper(index + 1, combination, combsum + candidates[index])
            combination.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            helper(index + 1, combination, combsum)
            
        helper(0, [], 0)
        return res