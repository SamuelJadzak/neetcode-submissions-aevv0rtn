class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits "67" -> "mp", "mq", "mr", "ms", "np"...
        # 6: mn, 7: pqr -> mp, mq, mr, np, nq, nr
        # digits is not empty
        dgt_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        if not digits:
            return res
        def helper(self, digits: str, perm: str) -> List[str]:
            if not digits:
                res.append(perm)
                return
            digit_letters = dgt_to_letters[digits[0]]
            # "mno"
            for char in digit_letters:
                # helper("7", "" + "m"), helper("7", "" + "n"), helper("7", "" + "o")
                helper(self, digits[1:], perm + char)
        # helper("67", "")
        helper(self, digits, "")
        return res
