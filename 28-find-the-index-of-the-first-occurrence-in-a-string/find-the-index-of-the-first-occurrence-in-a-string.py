class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firstChar = needle[0]
        needleSize = len(needle)
        haystackSize = len(haystack)
        for i in range(0, haystackSize - needleSize + 1):
            if haystack[i] != firstChar:
                continue
            else:
                if haystack[i : i + needleSize] == needle:
                    return i
        return -1