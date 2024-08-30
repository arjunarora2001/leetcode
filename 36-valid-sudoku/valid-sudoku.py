class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # BRUTE FORCE - individually check each row, column, box
        # However, that requires three passes
        # We could come up with a solution that uses only one pass
        # We could use a dictionary of sets
        rows = {i : set() for i in range(0, 9)}
        cols = {i : set() for i in range(0, 9)}
        boxes = {i : set() for i in range(0, 9)}
        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == '.':
                    continue
                if num in rows[row] or num in cols[col] or num in boxes[((row // 3) * 3 + col // 3)]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[((row // 3) * 3 + col // 3)].add(num)
        return True