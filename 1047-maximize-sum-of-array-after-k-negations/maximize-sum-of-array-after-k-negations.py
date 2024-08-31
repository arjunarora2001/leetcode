class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        if all positive:
            if k is even, return array as it is
            if k is odd:
                choose the minimum number:
                    flip the number
        """
        heapq.heapify(nums)
        while k > 0 and nums:
            elem = heapq.heappop(nums)
            if elem < 0:
                heapq.heappush(nums, elem * -1)
                k -= 1
            else:
                heapq.heappush(nums, elem)
                break
        if k % 2 != 0:
            nums[0] *= -1
        return sum(nums)