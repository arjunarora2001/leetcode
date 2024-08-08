class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            # need to error check here to avoid seg fault
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True