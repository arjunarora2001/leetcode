class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check the last element of each row
        # perform a binary search on the set of each last row's elements
        # if target > lastElem, move on to the next row
        # else, search that row

        # len(matrix) = numRows
        # len(matrix[0]) = numCols
        if target > matrix[-1][-1]:
            return False
        if target < matrix[0][0]:
            return False
        start = 0
        mid = 0
        end = len(matrix)
        while start < end:
            # if mid == start or mid == end:
            #     if matrix[mid][-1] == target:
            #         return True
            #     else:
            #         break
            mid = floor((start + end) / 2)
            tmp = matrix[mid][-1]
            if tmp == target:
                return True
            elif tmp < target:
                if target < matrix[mid + 1][-1]:
                    mid += 1
                    break
                elif target > matrix[mid + 1][-1]:
                    start = mid
                elif target == matrix[mid + 1][-1]:
                    return True
            elif tmp > target:
                if target > matrix[mid][0]:
                    break
                elif target < matrix[mid][0]:
                    end = mid 
                elif target == matrix[mid][0]:
                    return True
        # we now have the correct row. perform binary search again
        start = 0
        end = len(matrix[0])
        while start < end:
            rowMid = floor((start + end) / 2)
            if rowMid == start or rowMid == end:
                return False if matrix[mid][rowMid] != target else True
            if matrix[mid][rowMid] == target:
                return True
            elif matrix[mid][rowMid] > target:
                end = rowMid
            elif matrix[mid][rowMid] < target:
                start = rowMid
        return False