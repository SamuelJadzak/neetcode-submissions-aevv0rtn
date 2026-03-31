from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(res):
            if res == amount:
                return 0
            if res > amount:
                return -1
            
            min_coins = float('inf')
            for coin in coins:
                next_res = helper(res + coin)
                if next_res != -1:
                    min_coins = min(min_coins, next_res + 1)
            
            return min_coins if min_coins != float('inf') else -1
            
        return helper(0)