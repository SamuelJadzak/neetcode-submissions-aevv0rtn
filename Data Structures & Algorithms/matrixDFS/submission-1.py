class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        res = 0
        def dfs(coords, visited):
            nonlocal res
            if coords[0] == len(grid)-1 and coords[1] == len(grid[0])-1:
                res += 1
                return
            visited = visited + [coords]

            for i in range(coords[0]-1, coords[0]+2, 2):
                if 0 <= i < len(grid):
                    if grid[i][coords[1]] == 0 and (i, coords[1]) not in visited:
                        dfs((i, coords[1]), visited.copy())
            

            for j in range(coords[1]-1, coords[1]+2, 2):
                if 0 <= j < len(grid[0]): 
                    if grid[coords[0]][j] == 0 and (coords[0], j) not in visited:
                        dfs((coords[0], j), visited.copy())
        if grid[0][0] == 0:
            dfs((0,0), [])        
        return res