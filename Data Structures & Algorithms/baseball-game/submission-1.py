class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == "D":
                score.append(score[len(score)-1] * 2)
            elif op == "+":
                score.append(score[len(score)-1] + score[len(score)-2])
            elif op == "C":
                score.pop()
            else:
                score.append(int(op))
        return sum(score)
