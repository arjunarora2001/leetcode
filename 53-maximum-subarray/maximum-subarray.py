class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = 0
        currSum = 0
        for num in nums:
            currSum = max(currSum + num, 0) # we don't care about the current sum anymore and we can move our starting index forward
            maxSum = max(currSum, maxSum)
        if maxSum == 0:
            return max(nums)
        return maxSum