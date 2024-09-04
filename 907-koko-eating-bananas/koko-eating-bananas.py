class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPiles = max(piles)
        if h == len(piles):
            return maxPiles
        """
        sum(ceil(piles[i] / k)) == h
        find max val in piles
        calculate func for max val
        keep calculating for max val - 1 until we get an answer where calculated h > h
        """
        # [1,...,maxPiles] -> answer lies somewhere here
        minVal = maxPiles
        # lower bound
        left = ceil(sum(piles) / h)
        right = maxPiles
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)
            if hours > h:
                left = mid + 1
            elif hours <= h:
                minVal = min(minVal, mid)
                right = mid - 1
        return minVal