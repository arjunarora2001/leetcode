class Solution:
    def longestPalindrome(self, s: str) -> str:
        # test all len(s) strings
        # test all len(s) - 1 strings
        # test all len(s) - 2 strings
        # until len(s) - x == 0
        # return first palindrome
        if len(s) <= 1:
            return s
        def palindromeCheck(start: int, end: int) -> bool:
            # start = 0
            # end = len(s) - 1
            while start < end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    return False
            return True
        # if palindromeCheck(0, len(s) - 1):
        #     return s
        length = len(s) - 1
        for _ in range(len(s) - 1, 0, -1):
            start = 0
            end = length
            while end < len(s):
                if palindromeCheck(start, end):
                    return s[start:end + 1]
                start += 1
                end += 1
            length -= 1
        return s[0]