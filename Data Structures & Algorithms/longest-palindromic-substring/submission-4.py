class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = set()
        def helper(ind, subs):
            nonlocal res
            if subs == subs[::-1]:
                res.add(subs)
            if ind > len(s)-1:
                return
            if not subs:
                helper(ind+1, subs)
            helper(ind+1, subs+s[ind])
        helper(0, "")
        return max(res, key=len)