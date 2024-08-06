class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # numsTemp = set()
        # for i in nums:
        #     if i in numsTemp:
        #         return True
        #     else: 
        #         numsTemp.add(i)
        # return False
        return len(set(nums)) != len(nums)