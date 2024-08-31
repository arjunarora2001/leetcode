class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        rows = len(matrix)
        col = len(matrix[0]) - 1
        while row < rows and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False
        # def binarySearch(isRow: bool, index: int, start: int, end: int):
        #     # traverse the row of that index
        #     # row index stays constant; need to traverse through all the columns of that row
        #     if isRow:
        #         if start >= end:
        #             return False
        #         mid = (start + end) // 2
        #         if mid == end or mid == start:
        #             return False
        #         if matrix[index][mid] > target:
        #             binarySearch(True, index, start, mid)
        #         elif matrix[index][mid] < target:
        #             binarySearch(True, index, mid, end)
        #         else:
        #             return True


        #     # traverse the column of that index
        #     else:
        #         if start >= end:
        #             return False
        #         mid = (start + end) // 2
        #         if mid == end or mid == start:
        #             return False
        #         if matrix[mid][index] > target:
        #             binarySearch(False, index, start, mid)
        #         elif matrix[mid][index] < target:
        #             binarySearch(False, index, mid, end)
        #         else:
        #             return True
        # start = 0
        # for row in range(rows):
        #     if binarySearch(True, row, start, cols):
        #         return True
        #     start += 1
        #     if binarySearch(False, row, start, rows):
        #         return True
        # return False