class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # easy - use minHeap
        # heap will have k elements
        # sorted by distance from origin
        # if new point < last element in heap
        # have a maxHeap instead
        # heap will only ever have k elements at a time
        # if newPoint < maxHeap.top():
        #   heapq.heappush(newPoint)
        # at the end, just return the k-element heap
        def euclid(x, y):
            # x2 and y2 are always 0 since we start at origin
            return x ** 2 + y ** 2
        minHeap = []
        for x, y in points:
            heapq.heappush(minHeap, [euclid(x, y), [x, y]])
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        return ans