from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(res):
            # Base cases
            if res == amount:
                return 0  # Found exact amount, need 0 additional coins
            if res > amount:
                return -1  # Exceeded target amount
            
            min_coins = float('inf')
            for coin in coins:
                next_res = helper(res + coin)
                if next_res != -1:
                    min_coins = min(min_coins, next_res + 1)
            
            return min_coins if min_coins != float('inf') else -1
            
        return helper(0)