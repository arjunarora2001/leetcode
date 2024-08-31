class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 10 ** 4
        maximum = 0
        for price in prices:
            lowestPrice = min(price, lowestPrice)
            maximum = max(maximum, price - lowestPrice)
        return maximum