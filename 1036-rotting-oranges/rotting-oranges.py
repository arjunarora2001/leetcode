class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        def validCell(row: int, col: int) -> bool:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            return True
        # BFS:
        q = collections.deque()
        numFresh = 0
        minutes = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row, col])
                elif grid[row][col] == 1:
                    numFresh += 1
        if not q and numFresh == 0:
            return 0
        if not q and numFresh > 0:
            return -1
        minutes = 0
        while q and numFresh > 0:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for i, j in directions:
                    if validCell(row + i, col + j):
                        if grid[row + i][col + j] == 1:
                            q.append([row + i, col + j])
                            grid[row + i][col + j] = 2
                            numFresh -= 1
            minutes += 1
        return -1 if numFresh > 0 else minutes

        # ITERATIVE: 

        # have a boolean for whether anything has changed within a minute


        # numFresh = 0
        # changed = False
        # rows = len(grid)
        # cols = len(grid[0])
        # minutes = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 1:
        #             numFresh += 1
        # if numFresh == 0:
        #     return 0
        # while True:
        #     for row in range(rows):
        #         for col in range(cols):
        #             if grid[row][col] == 2:
        #                 for i, j in directions:
        #                     if validCell(row + i, col + j):
        #                         if grid[row + i][col + j] == 1:
        #                             grid[row + i][col + j] = -1
        #                             numFresh -= 1
        #                             if not changed:
        #                                 changed = True
        #     if not changed and numFresh > 0:
        #         return -1
        #     elif not changed:
        #         return minutes
        #     changed = False
        #     for row in range(rows):
        #         for col in range(cols):
        #             if grid[row][col] == -1:
        #                 grid[row][col] = 2
        #     minutes += 1
        # return minutes