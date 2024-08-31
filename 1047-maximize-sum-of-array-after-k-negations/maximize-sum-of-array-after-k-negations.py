class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        """
        if all positive:
            if k is even, return array as it is
            if k is odd:
                choose the minimum number:
                    flip the number
        """
        # k = k % len(nums) # if k is greater than length of numbers, we would be repeating negations which is unnecessary
        heapq.heapify(nums)
        kCopy = k
        for _ in range(kCopy):
            elem = heapq.heappop(nums)
            if elem < 0:
                elem *= -1
                heapq.heappush(nums, elem)
                k -= 1
            else:
                heapq.heappush(nums, elem)
                break
        if k % 2 == 0:
            return sum(nums)
        else:
            nums[0] *= -1
            return sum(nums)