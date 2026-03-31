class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                self.count += 1
                i -= 1
                j += 1
        
        self.count = 0
        for i in range(len(s)):
            helper(i, i) 
            helper(i, i+1)
        return self.count