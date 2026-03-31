class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def helper(ind, enc):
            if ind <= len(s)-1 and s[ind] == "0":
                return 0
            if ind >= len(s)-1:
                return 1
            
            if ind in cache:
                return cache[ind]
                
            result = helper(ind+1, enc + s[ind]) 
            if ind+1 < len(s) and int(s[ind:ind+2]) <= 26:
                result += helper(ind+2, enc + s[ind:ind+2])
            
            cache[ind] = result
            return result
            
        return helper(0, "")


        


