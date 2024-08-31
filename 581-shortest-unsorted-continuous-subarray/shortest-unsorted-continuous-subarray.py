class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = [] # stack of indices
        lower = len(nums) - 1
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                lower = min(stack.pop(), lower)
            stack.append(i)
        stack = []
        upper = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                upper = max(stack.pop(), upper)
            stack.append(i)
        return 0 if lower >= upper else upper - lower + 1