class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        have two pointers -> start and end (two elements apart)
        if nums[start] == nums[end], keep incrementing end until they're not equal
        once we know how many duplicate elements we have, bubble the window until the end of the list
        decrement size by the window size
        """
        size = len(nums)
        if size <= 2:
            return size
        start = 0
        end = 2
        while end < len(nums):
            # if nums[start] == (10 ** 4) + 1 or nums[end] == (10 ** 4) + 1:
            #     continue
            while nums[start] == nums[end]:
                nums[end] = (10 ** 4) + 1
                size -= 1
                if end + 1 < len(nums):
                    end += 1
                else:
                    break
            end += 1
            start = end - 2
            
        nums.sort()
        return size