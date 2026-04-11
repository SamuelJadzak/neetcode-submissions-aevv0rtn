class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        res = ""
        i = 0

        while i <= minLen - 1:
            res = res + word1[i] + word2[i]
            i += 1
        
        word1 = word1[i:]
        word2 = word2[i:]

        if word1:
            res = res + word1
        else:
            res = res + word2

        return res   
        