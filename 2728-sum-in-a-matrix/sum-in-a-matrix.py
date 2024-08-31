class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = [sorted(row) for row in nums]
        score = 0
        for i in range(len(rows[0])):
            rowMax = 0
            for j in range(len(rows)):
                if rows[j][i] > rowMax:
                    rowMax = rows[j][i]
            score += rowMax
        return score
        # score = 0
        # for operations in range(len(nums[0])):
        #     maxVal = 0
        #     for row in nums:
        #         rowMax = row[0]
        #         maxIndex = 0
        #         for i in range(1, len(row)):
        #             if row[i] > rowMax:
        #                 rowMax = row[i]
        #                 maxIndex = i
        #         row[maxIndex] = -1
        #         if rowMax > maxVal:
        #             maxVal = rowMax
        #     score += maxVal
        # return score
            