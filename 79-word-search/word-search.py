class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # start at board[0][0]
        # if board[0][0] == word[0]:
        #   move up if possible
        #   else move right
        #   else move down
        #   else move left
        # store last direction
        # base case: if i < 0 or i > len(board)
        # base case: if j < 0 or j > len(board[0])
        # base case: if board[i][j] != word[iterator]:
        #   ans.pop()
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(i, j, iterator):
            if iterator == len(word):
                return True
            if (i < 0 or i >= rows or j < 0 or j >= cols or (i, j) in path
                or word[iterator] != board[i][j]):
                return False
            path.add((i, j))
            check = (dfs(i - 1, j, iterator + 1) or
                    dfs(i, j + 1, iterator + 1) or
                    dfs(i + 1, j, iterator + 1) or
                    dfs(i, j - 1, iterator + 1))
            path.remove((i, j))
            return check
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, len(path)):
                    return True
        return False