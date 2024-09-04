class Solution:
    def climbStairs(self, n: int) -> int:
        # either take 1 or 2 steps
        if n <= 2:
            return n
        # keep it 1-indexed for simplicity
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]