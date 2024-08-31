class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = 0
        for operations in range(len(nums[0])):
            maxVal = 0
            for row in nums:
                rowMax = row[0]
                maxIndex = 0
                for i in range(1, len(row)):
                    if row[i] > rowMax:
                        rowMax = row[i]
                        maxIndex = i
                row[maxIndex] = -1
                if rowMax > maxVal:
                    maxVal = rowMax
            score += maxVal
        return score
            