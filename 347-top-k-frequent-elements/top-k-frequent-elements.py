class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        maxHeap = []
        for key, value in freq.items():
            heapq.heappush(maxHeap, (-value, key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans
