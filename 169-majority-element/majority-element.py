class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        size = len(nums)
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
            if d[i] > size/2:
                return i
        return 0