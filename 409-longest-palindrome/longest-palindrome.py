class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict(Counter(s))
        odd = 0
        for i in d.values():
            if i % 2 == 1:
                odd += 1
        if odd > 1:
            return len(s) - odd + 1
        return len(s)