class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xStr = str(x)
        start = 0
        end = len(xStr) - 1
        while start < end:
            if xStr[start] != xStr[end]:
                return False
            start += 1
            end -= 1
        return True