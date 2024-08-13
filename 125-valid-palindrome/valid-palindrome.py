class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].isalnum():
                if s[end].isalnum():
                    if s[start].lower() != s[end].lower():
                        return False
                else:
                    end -= 1
                    continue
            else:
                start += 1
                continue
            start += 1
            end -= 1
        return True