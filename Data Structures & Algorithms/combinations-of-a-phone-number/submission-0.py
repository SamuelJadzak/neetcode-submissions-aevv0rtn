class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {"2":["a","b","c"], "3":["d","e","f"],
        "4":["g","h","i"], "5":["j","k","l"], 
        "6":["m","n","o"], "7":["p","q","r","s"],
        "8":["t","u","v"], "9":["w","x","y","z"]}
        
        res = []
        def dfs(j, partition):
            if j >= len(digits):
                res.append(''.join(partition))
                return
            key = digits[j]
            for i, char in enumerate(keypad.get(key)):
                dfs(j+1, partition + [char])
        if digits:
            dfs(0, [])
        return res