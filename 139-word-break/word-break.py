class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        catsand, dict = ["cat", "cats", "and"]
        """

        """
        start from the back
        wordDict.length is only a maximum of 20, so compare substrings to the strings in the wordDict
        """

        # wordDict = set(wordDict) # need a hashset for faster lookups
        size = len(s)

        dp = [False] * (size + 1)
        dp[-1] = True

        for i in range(size, -1, -1):
            for w in wordDict:
                if dp[i] or (i + len(w)) > size:
                    continue
                if s[i : i + len(w)] == w:
                    # print(s[i : i + len(w)])
                    dp[i] = dp[i + len(w)]
                if dp[0] == True:
                    return True
        # print(dp)
        return dp[0]


        # UNFORTUNATELY, THE DFS SOLUTION GIVES ME A TLE. NEED TO USE DYNAMIC PROGRAMMING INSTEAD.
        # wordDict = set(wordDict)
        # end = False
        # def dfs(start: int):
        #     # print(start)
        #     nonlocal end
        #     if start >= len(s):
        #         end = True
        #         return
        #     for i in range(start, len(s)):
        #         if s[start : i + 1] in wordDict:
        #             dfs(i + 1) # start a new branch from that word onwards
        #             if end:
        #                 return
        #         # continue anyway and keep searching
        #     return
        # dfs(0)
        # return end
        