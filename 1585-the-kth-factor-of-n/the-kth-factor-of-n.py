class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # if k == 1:
        #     return 1
        # kCounter = 0
        # factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
        