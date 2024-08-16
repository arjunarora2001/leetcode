class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # d = dict(Counter(s))
        # valSet = set(d.values())
        # if len(valSet) != 1:
        #     return False
        # Not the end
        # Order matters too
        size = len(s)
        divider = 2
        while divider <= size:
            if size % divider == 0:
                index = int(size / divider)
                res = ""
                sub = s[0:index]
                for _ in range(divider):
                    res += sub
                if res == s:
                    return True
            divider += 1
        return False