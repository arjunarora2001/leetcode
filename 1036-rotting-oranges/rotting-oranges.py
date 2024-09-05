class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(row: int, col: int) -> bool:
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
        minutes = 0
        queue = collections.deque()
        numFresh = 0
        numRotten = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    numFresh += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
        if numFresh == 0:
            return 0
        while queue:
            minutes += 1
            # print(f"{minutes}, starting queue: {queue}")
            tmp = queue.copy()
            for _ in range(len(tmp)):
                row, col = queue.popleft()
                # up
                if isValid(row - 1, col) and grid[row - 1][col] == 1:
                    numFresh -= 1
                    grid[row - 1][col] = 2
                    queue.append((row - 1, col))
                # right
                if isValid(row, col + 1) and grid[row][col + 1] == 1:
                    numFresh -= 1
                    grid[row][col + 1] = 2
                    queue.append((row, col + 1))
                # down
                if isValid(row + 1, col) and grid[row + 1][col] == 1:
                    numFresh -= 1
                    grid[row + 1][col] = 2
                    queue.append((row + 1, col))
                # left
                if isValid(row, col - 1) and grid[row][col - 1] == 1:
                    numFresh -= 1
                    grid[row][col - 1] = 2
                    queue.append((row, col - 1))
            # print(f"{minutes}, ending queue: {queue}")
        if numFresh != 0:
            return -1
        else:
            return minutes - 1