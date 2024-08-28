class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = "" 
        # essentially a 26 base system with mapping to letters instead of numbers
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(columnNumber % 26 + ord('A')) + ans
            columnNumber //= 26
        return ans