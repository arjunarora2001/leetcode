class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digits = len(columnTitle)
        ans = 0
        for i in range(digits):
            number = ord(columnTitle[i]) - ord('A') + 1
            ans += (26 ** (digits - 1)) * number
            # print(ans)
            digits -= 1
        return ans