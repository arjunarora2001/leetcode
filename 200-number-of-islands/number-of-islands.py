class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do a DFS in all four directions from every point in the graph
        # keep searching until all land plots have been found
        # increment count from each point
        # dfs func must return a bool
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def isValid(row: int, col: int):
            if grid[row][col] != '1':
                return False
            return True

        def dfs(row: int, col: int) -> bool:
            if not isValid(row, col):
                return False
            grid[row][col] = '0'
            # north
            if row - 1 >= 0:
                dfs(row - 1, col)
            # east
            if col + 1 < cols:
                dfs(row, col + 1)
            # south
            if row + 1 < rows:
                dfs(row + 1, col)
            # west
            if col - 1 >= 0:
                dfs(row, col - 1)
            return True



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    if dfs(row, col):
                        islands += 1
        return islands