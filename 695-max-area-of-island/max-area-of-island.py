class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        
        def dfs(i: int, j: int):
            # beyond range of the grid, don't need to do anything
            if (i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in seen or grid[i][j] == 0):
                return 0
                
            seen.add((i, j))
            
            return (1 + dfs(i - 1, j) + 
                dfs(i, j + 1) + 
                dfs(i + 1, j) + 
                dfs(i, j - 1))

        maxAreaGlobal = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in seen:
                    maxAreaGlobal = max(maxAreaGlobal, dfs(i, j))
        return maxAreaGlobal