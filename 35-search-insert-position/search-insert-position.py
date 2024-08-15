class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if target > nums[-1]:
            return size
        elif target <= nums[0]:
            return 0
        # else, perform binary search
        start = 0
        end = size - 1
        mid = (start + end) // 2
        while start <= end:
            mid = (start + end) // 2
            midNum = nums[mid]
            if target == midNum:
                return mid
            elif target < midNum:
                end = mid - 1
            elif target > midNum:
                start = mid + 1
        return end + 1