class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # find first point of failure
        prev = nums[0]
        minIndex = -1
        maxIndex = -1
        for i in range(1, len(nums)):
            if prev > nums[i]:
                minIndex = i - 1
                break
            prev = nums[i]

        # list is already sorted
        if minIndex == -1:
            return 0
        
        prev = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            if prev < nums[i]:
                maxIndex = i + 1
                break
            prev = nums[i]

        # tentatively, answer is maxIndex - minIndex + 1
        # however, we still need to calculate the min and max to see where there are gaps

        minVal = min(nums[minIndex : maxIndex + 1])
        maxVal = max(nums[minIndex : maxIndex + 1])

        for i in range(minIndex):
            if nums[i] > minVal:
                minIndex = i
                break
        
        for i in range(len(nums) - 1, maxIndex - 1, -1):
            if nums[i] < maxVal:
                maxIndex = i
                break
        
        return maxIndex - minIndex + 1

        # stack = [] # stack of indices
        # lower = len(nums) - 1
        # for i in range(len(nums)):
        #     while stack and nums[stack[-1]] > nums[i]:
        #         lower = min(stack.pop(), lower)
        #     stack.append(i)
        # stack = []
        # upper = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         upper = max(stack.pop(), upper)
        #     stack.append(i)
        # return 0 if lower >= upper else upper - lower + 1