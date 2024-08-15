class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleSize = len(needle)
        if needleSize == 0:
            return 0
        firstChar = needle[0]
        for i in range(0, len(haystack) - needleSize + 1):
            if haystack[i] != firstChar:
                continue
            else:
                if haystack[i : i + needleSize] == needle:
                    return i
        return -1