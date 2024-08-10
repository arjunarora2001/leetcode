class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums: List[int], target: int, start: int, end: int) -> int:
            if start == end:
                return -1 if nums[start] != target else 0
            mid = floor((start + end) / 2)
            if mid == start or mid == end:
                return -1 if nums[mid] != target else 0
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(nums, target, mid, end)
            elif nums[mid] > target:
                return bs(nums, target, start, mid)
        if len(nums) == 1:
            return -1 if nums[0] != target else 0
        return bs(nums, target, 0, len(nums))