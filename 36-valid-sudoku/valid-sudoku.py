class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we know it's 9x9, so we can iterate through each box
        # BRUTE-FORCE:
        # iterate through each row
        # iterate through each column
        # iterate through each box
        # return false if any condition broken, else return true
        # very inefficient
        rows = collections.defaultdict(set)
        # row[0] = [5, 3, 7]
        cols = collections.defaultdict(set)
        # col[0] = [5, 6, 8, 4, 7]
        boxes = collections.defaultdict(set)
        # box[0] = [5, 3, 6, 9, 8]
        # boxNum = 0
        for i in range(len(board)):
            # boxNum += 1
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                boxNum = (i // 3, j // 3)

                if num in rows[i] or num in cols[j] or num in boxes[boxNum]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[boxNum].add(num)
        return True