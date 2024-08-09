class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # BRUTE FORCE: O(n^2)
        # Calculate every single combination and return largest
        size = len(prices)
        # maxProfit = 0
        # for i in range(size - 1):
        #     for j in range(i + 1, size):
        #         if prices[i] >= prices[j]:
        #             continue
        #         else:
        #             maxProfit = max(prices[j] - prices[i], maxProfit)
        # return maxProfit
        lowest = prices[0] # lowest UP UNTIL THAT POINT
        maxProfit = 0
        for i in range(size):
            maxProfit = max(maxProfit, prices[i] - lowest)
            lowest = min(lowest, prices[i])
        return maxProfit