class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def helper(stones):
            if not stones:
                return 0
            if len(stones) == 1:
                return stones[0]
            stones.sort()
            stone1, stone2 = stones[-1], stones[-2]
            if stone1 == stone2:
                stones = stones[:-2]
            elif stone1 < stone2:
                stones[-2] = stone2 - stone1
                stones = stones[:-1]
            else:
                stones[-1] = stone1 - stone2
                stones = stones[:-2] + stones[-1:]
            return helper(stones)
        return helper(stones)