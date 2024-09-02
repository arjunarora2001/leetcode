class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for preIndex in range(len(strs[0])):
            char = strs[0][preIndex]
            for s in strs:
                if preIndex == len(s) or s[preIndex] != char:
                    return pre
            pre += char
        return pre
