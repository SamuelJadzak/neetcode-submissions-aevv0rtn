class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        res = 0
        
        def landwalk(coords): 
            if grid[coords[1]][coords[0]] == "0": 
                return

            visited.append(coords) 
            
            for i in range(coords[1]-1, coords[1]+2, 2):
                if i >= 0 and i < len(grid):
                    if (coords[0], i) not in visited:
                        landwalk((coords[0], i))
            
            for j in range(coords[0]-1, coords[0]+2, 2): 
                if j >= 0 and j < len(grid[0]): 
                    if (j, coords[1]) not in visited:
                        landwalk((j, coords[1]))

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1" and (x, y) not in visited:
                    res += 1 
                    landwalk((x,y))
                    
        return res
