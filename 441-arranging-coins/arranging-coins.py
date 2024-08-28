class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        counter = 1
        while n > 0:
            n -= counter
            if n < 0:
                rows -= 1
            counter += 1
            rows += 1
        return rows