class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        char_set = set()
        l, r = 0, 1
        longest = 1
        char_set.add(s[l])
        while r < len(s):
            if s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            else:
                char_set.add(s[r])
                longest = max(r-l+1, longest)           
                r += 1
        return longest






