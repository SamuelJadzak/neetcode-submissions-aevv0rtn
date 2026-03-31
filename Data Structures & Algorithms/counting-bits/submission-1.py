class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0,n+1):
            res.append(0)
            num = bin(int(num))
            for char in num:
                if char == "1":
                    res[len(res)-1] += 1 
        return res

            