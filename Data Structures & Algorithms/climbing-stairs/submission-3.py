class Solution:
    def climbStairs(self, n: int) -> int:
        num_one = 1
        num_two = 1
        if not n:
            return 0
        if n == 1:
            return 1
        for i in range(n-2):
            temp = num_one
            num_one = num_one + num_two
            num_two = temp
            i += 1
        return num_one + num_two