class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for word in strs:
            cur = ""
            i = 0
            while True:
                if i >= len(lcp) or i >= len(word):
                    break
                if lcp[i] == word[i]:
                    cur = cur + lcp[i]
                else:
                    break
                i += 1
            lcp = cur
        return lcp
                
            
            
