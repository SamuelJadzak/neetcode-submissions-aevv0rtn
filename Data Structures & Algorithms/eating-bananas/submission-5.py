import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            mid = (l + r) // 2
            if self.canEatAll(piles, h, mid):
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        
        return res

    def canEatAll(self, piles: List[int], h: int, k: int) -> bool:
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / k)
            if hours > h:
                return False
        return True



