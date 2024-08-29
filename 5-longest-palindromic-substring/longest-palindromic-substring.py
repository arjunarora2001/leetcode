class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        size = len(s)
        # first calculate longest odd-numbered substrings
        for i in range(1, size):
            left = right = i
            while left - 1 >= 0 and right + 1 < size and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if right - left + 1 > len(longest):
                longest = s[left : right + 1]
                # print(f"Odd: {longest}")
        
        # now calculate longest even-numbered substrings
        for i in range(size - 1):
            left = i
            right = i + 1
            if s[left] == s[right]:
                if len(longest) < 2:
                    longest = s[left : right + 1]
                while left - 1 >= 0 and right + 1 < size and s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                if right - left + 1 > len(longest):
                    longest = s[left : right + 1]
                    # print(f"Even: {longest}")

        return longest