class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k >= len(nums):
            return nums
        freq = Counter(nums)
        maxHeap = []
        for key, value in freq.items():
            heapq.heappush(maxHeap, (-value, key))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])
        return ans
