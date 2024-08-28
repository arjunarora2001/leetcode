class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digits = len(columnTitle)
        ans = 0
        for i in range(digits):
            ans += (26 ** (digits - 1)) * (ord(columnTitle[i]) - ord('A') + 1)
            digits -= 1
        return ans