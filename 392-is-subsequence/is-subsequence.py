class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        startS = 0
        startT = 0
        while startT < len(t):
            if s[startS] == t[startT]:
                startS += 1
                if startS == len(s):
                    return True
            startT += 1
        return False