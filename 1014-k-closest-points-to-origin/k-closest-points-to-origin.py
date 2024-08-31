class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        for each point, calculate the distance from the origin
        then, put that into a minHeap with (distance, (x, y))
        then, k times, pop from the heap and append to a res array
        return res
        """
        distances = []
        for x, y in points:
            distances.append(((x ** 2) + (y ** 2), [x, y]))
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distances)[1])
        return res