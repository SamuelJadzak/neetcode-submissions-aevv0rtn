class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final_res = []
        
        def helper(i: int, curr_partition: List[str]):
            if i >= len(s):
                final_res.append(curr_partition[:])
                return
                
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr == substr[::-1]:
                    helper(j + 1, curr_partition + [substr])
        
        helper(0, [])
        return final_res