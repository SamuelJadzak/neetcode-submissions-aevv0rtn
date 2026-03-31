class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(i: int, curr_partition: List[str]):
            if i >= len(s):
                res.append(curr_partition.copy())
                return
                
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    helper(j + 1, curr_partition + [substr])
        
        helper(0, [])
        return res