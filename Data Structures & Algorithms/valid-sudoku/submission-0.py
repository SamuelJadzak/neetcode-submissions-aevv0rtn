class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                    
                box_id = (i // 3) * 3 + (j // 3)
                
                if (num in boxes[box_id] or num in rows[i] or num in cols[j]):
                    return False
                    
                boxes[box_id].add(num)
                rows[i].add(num)
                cols[j].add(num)
                
        return True