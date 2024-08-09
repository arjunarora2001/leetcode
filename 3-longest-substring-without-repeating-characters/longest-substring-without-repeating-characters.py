class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # Start at first character
        # Slide until a repeating character
        # Move start to one after the first repeated character
        # eg: babc -> b, a, b -> move start from b to a
        if len(s) < 1:
            return len(s)
        start = 0
        longest = 0
        strMap = {}
        for end in range(len(s)):
            if s[end] not in strMap:
                longest = max(longest, end - start + 1)
            else:
                if strMap[s[end]] < start:
                    longest = max(longest, end - start + 1)
                else:
                    start = strMap[s[end]] + 1
            strMap[s[end]] = end
        return longest