class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        preIndex = 0
        size = len(strs)
        while preIndex < len(strs[0]):
            char = strs[0][preIndex]
            for s in range(1, size):
                if preIndex >= len(strs[s]):
                    return pre
                if strs[s][preIndex] != char:
                    return pre
            pre += char
            preIndex += 1
        return pre
