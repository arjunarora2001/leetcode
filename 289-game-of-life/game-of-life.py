class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # We only need to find the NEXT state
        # Updated values should affect the next state in real time
        numLiveNeighbors = 0
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                numLiveNeighbors = 0
                # UP
                if row - 1 >= 0:
                    if abs(board[row - 1][col]) == 1:
                        numLiveNeighbors += 1
                    # UP RIGHT
                    if col + 1 < cols:
                        if abs(board[row - 1][col + 1]) == 1:
                            numLiveNeighbors += 1
                    # UP LEFT
                    if col - 1 >= 0:
                        if abs(board[row - 1][col - 1]) == 1:
                            numLiveNeighbors += 1
                # DOWN
                if row + 1 < rows:
                    if abs(board[row + 1][col]) == 1:
                        numLiveNeighbors += 1
                    # DOWN RIGHT
                    if col + 1 < cols:
                        if abs(board[row + 1][col + 1]) == 1:
                            numLiveNeighbors += 1
                    # DOWN LEFT
                    if col - 1 >= 0:
                        if abs(board[row + 1][col - 1]) == 1:
                            numLiveNeighbors += 1
                # LEFT
                if col - 1 >= 0:
                    if abs(board[row][col - 1]) == 1:
                        numLiveNeighbors += 1
                # RIGHT
                if col + 1 < cols:
                    if abs(board[row][col + 1]) == 1:
                        numLiveNeighbors += 1
                
                # live cell
                if abs(board[row][col]) == 1:
                    if numLiveNeighbors < 2 or numLiveNeighbors > 3:
                        board[row][col] = -1
                # dead cell
                else: 
                    if numLiveNeighbors == 3:
                        board[row][col] = 2
        for i in range(rows):
            for j in range(cols):
                if board[i][j] >= 1:
                    board[i][j] = 1
                else:
                    board[i][j] = 0