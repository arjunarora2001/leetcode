class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        # create a max heap
        heapq.heapify(stones)
        while len(stones) > 1:
            firstStone = -heapq.heappop(stones)
            secondStone = -heapq.heappop(stones)
            print(f"{firstStone}, {secondStone}")
            # firstStone >= secondStone
            if firstStone > secondStone:
                heapq.heappush(stones, -(firstStone - secondStone))
        if stones:
            return -stones[0]
        return 0