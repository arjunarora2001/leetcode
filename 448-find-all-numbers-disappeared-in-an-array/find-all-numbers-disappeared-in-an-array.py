class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numSet = set(nums)
        n = len(nums)
        ans = []
        for i in range(1, n + 1):
            if i not in numSet:
                ans.append(i)
        return ans