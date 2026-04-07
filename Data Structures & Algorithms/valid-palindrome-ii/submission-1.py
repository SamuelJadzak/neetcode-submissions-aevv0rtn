class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i, char in enumerate(s):
            res = True
            sCharRemoved = s[:i] + s[i+1:]
            p1 = 0
            p2 = len(sCharRemoved)-1
            while p2 > p1:
                if sCharRemoved[p1] != sCharRemoved[p2]:
                    res = False
                    break
                p1 += 1
                p2 -= 1
            if res:
                return res
        return res