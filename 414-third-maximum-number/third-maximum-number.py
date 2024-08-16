class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSet = set(nums)
        numSet = sorted(numSet)
        if len(numSet) < 3:
            return numSet[-1]
        return numSet[-3]
