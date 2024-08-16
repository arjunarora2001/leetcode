class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # have a boolean for whether anything has changed within a minute
        def validCell(row: int, col: int) -> bool:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            return True

        numFresh = 0
        changed = False
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0 # incorrect since we could start with 0 fresh oranges
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    numFresh += 1
        if numFresh == 0:
            return 0
        while True:
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 2:
                        for i, j in directions:
                            if validCell(row + i, col + j):
                                if grid[row + i][col + j] == 1:
                                    grid[row + i][col + j] = -1
                                    numFresh -= 1
                                    if not changed:
                                        changed = True
            if not changed and numFresh > 0:
                return -1
            elif not changed:
                return minutes
            changed = False
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == -1:
                        grid[row][col] = 2
            minutes += 1
        return minutes