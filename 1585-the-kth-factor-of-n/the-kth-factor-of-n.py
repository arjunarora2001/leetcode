class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # if k == 1:
        #     return 1
        # kCounter = 0
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
                if len(factors) == k:
                    return max(factors)
        return -1
        