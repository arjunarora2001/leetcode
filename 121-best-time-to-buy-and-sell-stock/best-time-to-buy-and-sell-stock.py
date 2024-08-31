class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = 10 ** 4
        maximum = 0
        for price in prices:
            lowestPrice = min(price, lowestPrice)
            maximum = max(maximum, price - lowestPrice)
        return maximum
        # size = len(prices)
        # j = 1
        # i = 0
        # while j < size and i < size - 1:
        #     if prices[j] <= prices[i]:
        #         j += 1
        #         i += 1
        #     else:
        #         break
        # if j == size:
        #     return 0
        # maximum = 0
        # minVal = min(prices)
        # for i in range(j - 1, size - 1):
        #     localMax = max(prices[i + 1 : size]) - prices[i]
        #     if localMax <= 0:
        #         continue
        #     else:
        #         if prices[i] == minVal and localMax > maximum:
        #             return localMax
        #         else:
        #             maximum = max(maximum, localMax)
        # return maximum