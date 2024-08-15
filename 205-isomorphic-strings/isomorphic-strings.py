class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sd = {}
        td = {}
        for i in range(len(s)):
            if s[i] not in sd and t[i] not in td:
                sd[s[i]] = t[i]
                td[t[i]] = s[i]
            elif t[i] in td:
                if td[t[i]] != s[i]:
                    return False
            elif s[i] in sd:
                if sd[s[i]] != t[i]:
                    return False
        return True