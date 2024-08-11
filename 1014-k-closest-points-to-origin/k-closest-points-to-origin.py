class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(x, y):
            # x2 and y2 are always 0 since we start at origin
            return x ** 2 + y ** 2
        minHeap = []
        for x, y in points:
            minHeap.append([euclid(x, y), [x, y]])
            # heapq.heappush(minHeap, [euclid(x, y), [x, y]])
        heapq.heapify(minHeap)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        return ans