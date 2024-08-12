class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        seen = set()
        numIslands = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            if (i, j) in seen:
                return False
            # Process coordinate
            seen.add((i, j))
            # don't care if it's 0 (water)
            if grid[i][j] == '0':
                return False
            # Process up
            dfs(i - 1, j)
            # Process right
            dfs(i, j + 1)
            # Process down
            dfs(i + 1, j)
            # Process left
            dfs(i, j - 1)
            if grid[i][j] == '1':
                return True
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in seen and grid[i][j] == '1':
                    if dfs(i, j):
                        numIslands += 1
        return numIslands
            