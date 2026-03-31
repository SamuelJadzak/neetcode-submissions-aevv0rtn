class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] means s[:i] can be segmented
        dp[0] = True  # empty string is always valid
        
        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)]:
                    if s[i - len(word):i] == word:
                        dp[i] = True
                        break
        
        return dp[n]
        