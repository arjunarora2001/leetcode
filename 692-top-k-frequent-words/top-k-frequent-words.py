class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        minHeap = []
        for key, value in freq.items():
            heapq.heappush(minHeap, (-value, key))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res