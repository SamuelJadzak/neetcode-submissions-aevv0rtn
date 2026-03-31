class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        def helper(row, column, ind, visited):
            nonlocal res
            # print(board[row][column])
            if (row, column) in visited:
                return
            if board[row][column] != word[ind]:
                return
            if ind == len(word)-1:
                res = True
                return
            visited.add((row,column))

            if (row - 1 >= 0):
                helper(row-1, column, ind+1, visited)
            if (row + 1 < len(board)):
                helper(row+1, column, ind+1, visited)
            if (column - 1 >= 0):
                helper(row, column-1, ind+1, visited)
            if (column + 1 < len(board[row])):
                helper(row, column+1, ind+1, visited)

            visited.remove((row,column))

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == word[0]:
                    print(board[row][column])
                    helper(row, column, 0, set())
        
        return res
        

        