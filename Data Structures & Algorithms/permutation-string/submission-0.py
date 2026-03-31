from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = defaultdict(int)
        for char in s1:
            s1_chars[char] += 1
        print(s1_chars)
        l, r = 0, len(s1)-1
        while r < len(s2):
            s2_chars = defaultdict(int)
            temp = l
            while temp <= r:
                s2_chars[s2[temp]] += 1
                temp += 1
            print(s2_chars)
            if s1_chars == s2_chars:
                return True
            l += 1
            r += 1
        return False


