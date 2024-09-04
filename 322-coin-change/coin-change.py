class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [2 ** 31] * (amount + 1)
        """
        dp[0] = 1 coin of 1
        dp[1] = 1 coin of 2
        dp[2] = 1 coin of 2, 1 coin of 1 => 3
        """
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] > amount + 1 else dp[-1]