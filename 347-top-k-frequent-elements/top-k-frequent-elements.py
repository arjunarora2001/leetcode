class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums
        freq = Counter(nums)
        # minHeap of only k elements
        minHeap = []
        for key, value in freq.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        return ans
