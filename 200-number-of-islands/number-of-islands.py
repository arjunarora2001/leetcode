class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # do a DFS in all four directions from every point in the graph
        # keep searching until all land plots have been found
        # increment count from each point
        # dfs func must return a bool
        seen = set()
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def isValid(row: int, col: int):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in seen or grid[row][col] != '1':
                return False
            seen.add((row, col))
            return True

        def dfs(row: int, col: int) -> bool:
            if not isValid(row, col):
                return False
            # north
            dfs(row - 1, col)
            # east
            dfs(row, col + 1)
            # south
            dfs(row + 1, col)
            # west
            dfs(row, col - 1)
            return True



        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == '1':
                    if dfs(row, col):
                        islands += 1
        return islands